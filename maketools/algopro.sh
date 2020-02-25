#!/bin/bash

set -e

# Set environment
export AP_BASEDIR=${PWD}
export AP_ACTION="${AP_ACTION:-$1}"

# Source helper funcs
source ${AP_BASEDIR}/maketools/_sourced/helpers.sh
_run_all_helpers

###
### Deps
###
if [ "${AP_ACTION}" == "deps" ]; then
    pip3 install --user -U pipenv pip
    if [ ! -d "${AP_BASEDIR}/.venv" ]; then
        _warn_msg "Installing python dependencies with pipenv, please be patient..."
        pipenv install --dev
    else
        _warn_msg "Updating python dependencies with pipenv, please be patient..."
        pipenv update
        pipenv clean
    fi

###
### Lint
###
elif [ "${AP_ACTION}" == "lint" ]; then
    ${pipenv} flake8 --exclude=.venv/ --statistics --show-source --max-line-length=80 .
    ${pipenv} pylint src tests

###
### Test
###
elif [ "${AP_ACTION}" == "test" ]; then
    ${pipenv} pytest -v
fi
