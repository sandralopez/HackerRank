#!/bin/bash

read N

if [ $N -gt 500 ] || [ $N -lt 1 ]
then 
    echo "Error"
else 
    suma=0
    total=$N 

    while [ $N -gt 0 ]
    do
        read X
        
        if [ $X -lt 10000 ] || [ $X -gt -10000 ]
        then
            suma=$(($suma + $X))
        else
             ((total--))
        fi
        
        ((N--))
    done

    if [ $total -gt 0 ]
    then
        printf "%.3f" $(echo $suma / $total | bc -l)
    else
        echo "Error"
    fi
fi