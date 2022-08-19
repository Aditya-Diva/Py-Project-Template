#!/bin/bash

# This should be run from main/root directory

# Run sphinx-apidoc command
# -f for forcing creation of .rst files
# -o for path to dump generated .rst files (output)
# last argument is the input, here we make it pick up
# folders(submodules) from the lib folder/module one by one.

# This path is the lib module which contains other modules in this case
sphinx-apidoc -f -o docs/source/ lib/;

# Option: For individual folders
# Find directory types at ../lib/ and exec the commands over the outputs
# find ../lib/ -type d -exec sphinx-apidoc -f -o source/ {} \;

# Actually generate the html file here
cd docs/
make clean html
make html
