#!/bin/sh

width=`tput cols`

# simple example to graph the du command output

# run du -> refomart a little with awk -> give it to asciigraph
du -d 1 $@ | head -n -1 |\
    awk '{s = ""; for (i = 2; i <= NF; i++) s = s $i " "; printf "%s:%s\n", s, $1 * 1024;}' | \
    asciigraph -l 'Disk Usage' -H -s dec -c -w $width
