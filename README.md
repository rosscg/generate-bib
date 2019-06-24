
# generate-bib

This script takes uses the gscholar package to create a .bib file for a set of pdf files and/or paper titles.


### Requirements:

* On MacOS X, install [poppler](https://poppler.freedesktop.org/):

	`brew install pkg-config poppler`

*  Install gscholar:

	`pip install gscholar`

### Use:

* Put pdfs in directory `./input/`
* Enter paper details on single lines in `./input/papers.txt`.
* Run script, bib output will be `./output/library.bib`,
* Papers which were not found will be listed in `./output/failed.txt`
* Manually check the bib for errors.
