#!/usr/bin/env python3


input_file = "./uBlacklist.txt"
with open(input_file, "r") as fp:
    lines = fp.readlines()
    new_lines = []
    for line in lines:
        # - Strip white spaces
        line = line.strip()
        if line not in new_lines:
            if len(line) == 0:
                continue
            if line[0] not in ["\n", '#']:
                new_lines.append(line)

output_file = "output.txt"
with open(output_file, "w") as fp:
    fp.write("\n".join(sorted(new_lines)))
