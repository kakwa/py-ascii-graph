#!/bin/sh

# It's a small example of asciigraph usage
# It just displays the load

#get number of cores (empiricaly I always try to have load < number of cores)
max=`cat /proc/cpuinfo|grep processor|wc -l`

while true
do
    #get the load
    load_15=`uptime|sed "s/.*:\ //"|cut -d ',' -f 3`
    load_1=`uptime|sed "s/.*:\ //"|cut -d ',' -f 1`
    load_5=`uptime|sed "s/.*:\ //"|cut -d ',' -f 2`

    #get the width
    width=`tput cols`

    #get the number of char to rewrite
    char=$(( $width * 5 + 7 ))
    printf \
       "load threshold:$max\n\
        load last minute:$load_1\n\
        load last 5 minutes:$load_5\n\
        load last 15 minutes:$load_15\n" | asciigraph -w $width -l 'loadtop'

    #going back to where we start writing (overwrite the lines)
    counter=0
    while [ $counter -ne $char ]
    do
        printf "\b"
        counter=$(( $counter + 1  ))
    done

    #refresh every 1 second
    sleep 1
done
