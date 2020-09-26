#!/bin/bash

for dir in * ; do
  if [ -d "$dir" ] ; then
    # replace white space to underscore
    new_dir=${dir// /_}
    mv "$dir" "$new_dir" || echo 'Could not remove whitespace of "$dir"'
  fi
done
