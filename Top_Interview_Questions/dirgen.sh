#!/bin/bash

mkdir "$*" && touch "$*/problem.txt" && touch "$*/solution.py" && code "$*/problem.txt" && code "$*/solution.py"