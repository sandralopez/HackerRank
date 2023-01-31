#!/bin/bash

read M

printf "%.3f" $(echo $M | bc -l)