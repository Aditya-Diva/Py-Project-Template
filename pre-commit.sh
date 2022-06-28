#!/bin/bash

# To remove trouble-making cache (if need be)
# pre-commit clean
# pre-commit autoupdate

# To install pre-commit into git hooks.
pre-commit install
# To manually run pre-commit hooks on repo
pre-commit run --all-files
