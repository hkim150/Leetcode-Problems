#!/bin/bash

str="$*"

# replace white space to underscore
str=${str// /_}

mkdir "$str" && touch "$str/problem.txt" && touch "$str/solution.py" && code "$str/problem.txt" && code "$str/solution.py"
