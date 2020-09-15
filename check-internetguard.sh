#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

function usage() {
    echo "Usage: $0 <domain> [<domains>]"
}

function check_internetguard() {
    ip=`dig @dns1.bluewin.ch +short "$1"`
    [[ $ip == 195.186* ]]
}

if [[ "$#" -lt 1 ]]; then
    usage
    exit 1
fi

if [[ "$1" == -h ]]; then
    usage
    exit 0
fi

for domain in "$@"; do
    if check_internetguard $domain; then
        echo -ne "${RED}block${NC}"
    else
        echo -ne "${GREEN}pass${NC}"
    fi
    echo -e "\t$domain"
done
