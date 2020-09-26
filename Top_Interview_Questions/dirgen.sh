#!/bin/bash

str="$*"

# replace white space to underscore
str=${str// /_}

mkdir "$str" && touch "$str/problem.txt" && touch "$str/solution.py" && touch "$str/solution.java" && idea "$str/problem.txt" && idea "$str/solution.py" && idea "$str/solution.java"
