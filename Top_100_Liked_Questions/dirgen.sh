#!/bin/bash

str="$*"

# replace white space to underscore
str=${str// /_}

mkdir "$str" && touch "$str/problem.txt" && touch "$str/solution.py" && touch "$str/solution.js" && code "$str/problem.txt" && code "$str/solution.py" && code "$str/solution.js"
