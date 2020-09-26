#!/bin/bash

str="$*"

# replace white space to underscore
str=${str// /_}

touch "$str/solution.java"

for f in $str/*
do
  echo "$f"
  idea "$f"
done
