#!/bin/bash

# Loop through all Python files in the current directory
for python_file in *.py; do
  # Skip hidden files starting with "_"
  if [[ $python_file == _* ]]; then
    continue
  fi

  # Run the Python file
  echo "Running ${python_file}..."
  python3 "${python_file}"
done