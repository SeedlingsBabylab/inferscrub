import sys
import os
import os
import subprocess as sp
import regex as re
import csv

start_rgx = re.compile(
    "(silence_start:\\s+)(-?\d*\.?\d+)")
end_rgx = re.compile(
    "(silence_end:\\s+)(-?\d*\.?\d+)")


def infer(path):
    command = ["ffmpeg", "-i", path, "-af",
               "silencedetect=n=-70dB:d=5",
               "-f", "null", "-"]

    pipes = sp.Popen(
        command, stdout=sp.PIPE, stderr=sp.PIPE)
    std_out, std_err = pipes.communicate()
    start = re.findall(start_rgx, std_err)
    end = re.findall(end_rgx, std_err)

    if len(start) != len(end):
        raise Exception("start/end count mismatch: {}".format(path))

    joined = zip([float(x[1]) for x in start], [float(x[1]) for x in end])

    return joined


if __name__ == "__main__":
    input_dir = sys.argv[1]

    results = []

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".wav"):
                sils = infer(os.path.join(root, file))
                res = [(file, i, j) for i, j in sils]
                print res
                results.extend(res)

    with open("silences.csv", "wb") as out:
        writer = csv.writer(out)
        writer.writerow(["file", "onset", "offset"])
        writer.writerows(results)
