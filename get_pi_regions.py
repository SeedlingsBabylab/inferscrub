import sys
import os
import csv
import pyclan as pc


def extract_pi_regions(path):
    cf = pc.ClanFile(path)
    begin = [x for x in cf.line_map if "begin personal" in x.line]
    end = [x for x in cf.line_map if "end personal" in x.line]

    if len(begin) != len(end):
        joined = begin + end
        joined.sort(key=lambda x: x.onset)
        with open(os.path.join("errors", "{}_pi_errors".format(os.path.basename(path)[:5])), "wb") as out:
            for x in joined:
                out.write(
                    "{} - {}\n".format(x.line.replace("\n", ""), x.timestamp()))
        raise Exception(
            "Begin and End comment count mismatch: {}".format(os.path.basename(path)))

    joined = [(os.path.join(path), x[0].onset, x[1].onset)
              for x in zip(begin, end)]

    for x in joined:
        if not x[1] < x[2]:
            joined = begin + end
            joined.sort(key=lambda x: x.onset)
            with open(os.path.join("errors", "{}_pi_errors".format(os.path.basename(path)[:5])), "wb") as out:
                for x in joined:
                    out.write(
                        "{} - {}\n".format(x.line.replace("\n", ""), x.timestamp()))
            raise Exception(
                "End comment precedes Begin:           {}".format(os.path.basename(path)))

    return joined


if __name__ == "__main__":
    input_dir = sys.argv[1]

    regions = []
    results = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".cha"):
                try:
                    regs = extract_pi_regions(os.path.join(root, file))
                    regions.extend(regs)
                except Exception as e:
                    print e

    with open("pi_regions.csv", "wb") as out:
        writer = csv.writer(out)
        writer.writerow(["file", "onset", "offset"])
        writer.writerows(regions)
