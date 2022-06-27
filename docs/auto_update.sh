#!/bin/bash

# Run sphinx-apidoc command
# -f for forcing creation of .rst files
# -o for path to dump generated .rst files (output)
# last argument is the input, here we make it pick up 
# folders(modules) from the lib file one by one.
sphinx-apidoc -f -o source/ ../lib/*

# Actually generate the html file here
make html