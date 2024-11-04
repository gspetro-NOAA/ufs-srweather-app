#!/bin/bash
# This script rebuilds technical documentation for the ush and tests/WE2E Python scripts
# The build will fail if there are warnings. 
# Warnings may be caused by incomplete or nonexistent documentation
# as well as by minor issues such as broken external links that need to be fixed or removed

# Install prerequisites
sudo apt-get install python3-sphinx
sudo apt-get install python3-sphinx-rtd-theme
pip install sphinxcontrib-bibtex

# Remove existing directories
cd doc/TechDocs
rm -rf ush
rm -rf tests/WE2E

# Regenerate tech docs in ush and tests/WE2E based on current state of scripts in those directories.
sphinx-apidoc -fM -o ./ush ../../ush
sphinx-apidoc -fM -o ./tests/WE2E ../../tests/WE2E
ls ush

# Check for mismatch between what comes out of this action and what is in the PR. 
diff=`git diff`
echo "${diff}"
git status


# Check output from git diff command^ Why no diff on calculate_cost.rst?


# May be able eventually to add an action that adds the properly built docs to the PR or the target branch

