#!/bin/bash
# This script rebuilds technical documentation for the ush and tests/WE2E Python scripts
# The build will fail if there are warnings. 
# Warnings may be cause by incomplete or nonexistent documentation
# as well as by minor issues such as broken external links that need to be fixed or removed


# Install prerequisites
sudo apt-get install python3-sphinx
#sphinx_rtd_theme
#sphinxcontrib-bibtex


# Remove existing directories
cd doc/TechDocs
rm -rf ush
rm -rf tests

# Regenerate docs in ush and tests/WE2E based on current state of scripts in those directories.
sphinx-apidoc -fM -o ./TechDocs/ush ../ush
sphinx-apidoc -fM -o ./TechDocs/tests/WE2E ../tests/WE2E

# Need to check if there's a mismatch between what comes out of this build 
# and what is in the PR. 

# May be able eventually to add an action that adds the properly built docs to the PR or the target branch

