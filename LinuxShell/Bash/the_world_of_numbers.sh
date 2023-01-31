#!/bin/bash

read X
read Y


if [ $X -gt 100 ] || [ $X -lt -100 ] || [ $Y -gt 100 ] || [ $Y -lt -100 ] || [ $Y -eq 0 ]
then
    echo 'Input format error'
else
    # Sum
    echo $(expr $X + $Y)


    # Diff
    echo $(expr $X - $Y)


    # Prod
    echo $(expr $X \* $Y)


    # Quotient
    echo $(expr $X \/ $Y)
fi
