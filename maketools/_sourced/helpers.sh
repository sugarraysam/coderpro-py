#!/bin/bash

###
### Vars
###
RED=1
GREEN=2
YELLOW=3

###
### Funcs
###
_err_msg() {
    echo >&2 "$(
        tput bold
        tput setaf ${RED}
    )[-] ERROR: ${*}$(tput sgr0)"

    exit 1337
}

_warn_msg() {
    echo >&2 "$(
        tput bold
        tput setaf ${YELLOW}
    )[!] WARNING: ${*}$(tput sgr0)"
}

_info_msg() {
    echo >&2 "$(
        tput bold
        tput setaf ${GREEN}
    )[] INFO: ${*}$(tput sgr0)"
}

_run_all_helpers() {
    _setup_pipenv # must be first
    _check_python_venv
}

_setup_pipenv() {
    export PIPENV_VENV_IN_PROJECT=1

    # Not using pipenv inside CI because it is too slow
    if [ "${CI}" == "true" ]; then
        pipenv=""
    else
        pipenv="pipenv run"
    fi
}

_check_python_venv() {
    if [ ! -d "${AP_BASEDIR}/.venv" ] && [ "${AP_ACTION}" != "deps" ] && [ "${CI}" != "true" ]; then
        _err_msg "Python venv not found, please run 'make deps'"
    fi
}
