# This script takes uses the gscholar package to create a
# .bib file for a set of pdf files and/or paper titles.
# Written by Ross Gales github.com/rosscg
#
#
# On MacOS X, install poppler:
# > brew install pkg-config poppler
#
# Then install gscholar:
# > pip install gscholar
#
# Put pdfs in directory ./input/
# Enter paper details on single lines in ./input/papers.txt.
# Run script, bib output will be ./output/library.bib,
# Papers which were not found will be listed in ./output/failed.txt
# Manually check the bib for errors.

import gscholar
from os import listdir
from os.path import isfile, join

input_dir = "input/"
output_dir = "output/"
bib_list = set()
failed_list = []

# Get bib entries for pdfs in ./pdf-files/:
pdffiles = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]
for file in pdffiles:
    entry = gscholar.pdflookup(input_dir + file, allresults=False, outformat=4)[0]
    bib_list.add(entry)

# Get bib entries for titles in papers.txt:
try:
    f = open(join(input_dir, 'papers.txt'), "r")
    papers = f.read().split("\n")
    f.close
except Exception as e:
    papers = []
for p in papers:
    if p == "":
        continue
    try:
        entry = gscholar.query(p)[0]
        bib_list.add(entry)
    except IndexError as e:
        print("Bad input line: {}".format(p))
        failed_list.append(p)

# Print bib file
if len(bib_list) > 0:
    with open(join(output_dir, "library.bib"), "w+") as f:
        f.write("The following entries have been generated by a script and therefore should be checked for accuracy.\nCreated by Ross Gales, https://github.com/rosscg/generate-bib\n\n")
        for l in bib_list:
            f.write(l)
    f.close()

# Print failed lines to file
if len(failed_list) > 0:
    with open(join(output_dir, "failed.txt"), "w+") as f:
        f.write("The following papers were not found:\n\n")
        for l in failed_list:
            f.write(l + '\n\n')
    f.close()
