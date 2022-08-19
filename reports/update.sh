#!/bin/bash

# This should be run from main/root directory

# In order to run this in reports folder uncomment the cd .. below
# cd ..

# Pytest (Kept for reference)
# --html -> Where to save the generate html
# Path to tests to be run
# pytest --html=reports/pytest/pytest.html tests/

# Pytest Coverage
# -q -> quiet / less verbose
# --html -> Where to save the generate html(Pytest report)
# --cov -> Which module do we want to cover
# --cov-report -> Type of output format:destination
# --cov-config -> Provide path to config (.coveragerc)
# Path to tests that cover the module
pytest -q --html=reports/pytest/index.html --cov=lib --cov-report=html:reports/pytestcov/ --cov-config=reports/.coveragerc tests/

# Adding command a second time so it's generated in the docs folder (For github gh-pages)
pytest -q --html=docs/reports/pytest/index.html --cov=lib --cov-report=html:docs/reports/pytestcov/ --cov-config=reports/.coveragerc tests/
