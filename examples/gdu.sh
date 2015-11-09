#!/bin/sh

# simple example to graph du output

exit_err(){
    msg=$1
    printf "$msg\n"
    exit 1
}

dir='./'
! [ -z "$@" ] && dir="$@"

[ -e "$dir" ] || exit_err "Directory '$dir' doesn't exist"

du -d 1 "$dir" | \
    awk '{printf "%s:%s\n", $2, $1 * 1024;}' |\
    asciigraph -l 'Disk Usage' -H -s dec
