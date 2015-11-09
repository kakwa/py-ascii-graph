#!/bin/sh

# simple example to graph the du command output

exit_err(){
    msg=$1
    printf "$msg\n"
    exit 1
}

# default dir to study
dir='./'
# taking all the arguments as one
! [ -z "$@" ] && dir="$@"

# exit if argument is not a directory
[ -e "$dir" ] || exit_err "Directory '$dir' doesn't exist"

# run du -> refomart a little with awk -> give it to asciigraph
du -d 1 "$dir" | \
    awk '{printf "%s:%s\n", $2, $1 * 1024;}' | \
    asciigraph -l 'Disk Usage' -H -s dec
