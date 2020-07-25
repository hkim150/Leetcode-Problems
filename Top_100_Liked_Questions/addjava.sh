#!/bin/bash

str="$*"

# replace white space to underscore
str=${str// /_}

touch "$str/solution.java" && idea "$str/solution.java"
