#!/bin/bash

read X
read Y
read Z

if [ $X -lt 1 ] || [ $X -gt 1000 ] || [ $Y -lt 1 ] || [ $Y -gt 1000 ] || [ $Z -lt 1 ] || [ $Z -gt 1000 ]
then
    echo "Error"
else
    if [ $X -eq $Y ] && [ $X -eq $Z ]
    then
        echo "EQUILATERAL"
    elif [ $X -eq $Y ] || [ $Y -eq $Z ] || [ $X -eq $Z ]
    then 
        echo "ISOSCELES"
    else 
        echo "SCALENE"
    fi
fi
