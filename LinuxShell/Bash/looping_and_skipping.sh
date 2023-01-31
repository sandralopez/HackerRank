#!/bin/bash

N=1
while [ $N -lt 100 ]
do
    if [ $(expr $N % 2) -ne 0 ] 
    then
        echo $N
    fi
    N=$(expr $N + 1)
done
