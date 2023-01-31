#!/bin/bash

read C

if [ "$C" == "Y" ] || [ "$C" == "y" ]
then
    echo "YES"
elif [ "$C" == "N" ] || [ "$C" == "n" ]
then
    echo "NO"
else
    echo "Error"
fi
