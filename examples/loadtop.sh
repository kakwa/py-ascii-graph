#!/bin/sh

# It's a small example of asciigraph usage
# It just displays the load

tput clear
old_width=`tput cols`


# Get number of cores (empiricaly I always try to have load < number of cores)
max=`grep -c processor /proc/cpuinfo`
# Calculate the first threshold (until this threshold, graph is green)
t1=`awk "BEGIN {print $max * 3 / 4}"`
# Calculate the second threshold.
# Between t1 and t2, graph is yellow. 
# After t2, graph is red.
t2=`awk "BEGIN {print $max * 4 / 4}"`

while true
do
    # Get the load
    load_15=`uptime|sed "s/.*:\ //"|cut -d ',' -f 3`
    load_1=`uptime|sed "s/.*:\ //"|cut -d ',' -f 1`
    load_5=`uptime|sed "s/.*:\ //"|cut -d ',' -f 2`

    # Get the width of the term
    width=`tput cols`
    if [ $width -ne $old_width ]
    then
        tput clear
    fi
    old_width=$width

    printf "\
load threshold:$max\n\
load last minute:$load_1\n\
load last 5 minutes:$load_5\n\
load last 15 minutes:$load_15\n" | \
    asciigraph -w $width -l 'loadtop' -c -t $t1 -T $t2

    #refresh every 1 second
    tput cup 0 0
    sleep 1
done
