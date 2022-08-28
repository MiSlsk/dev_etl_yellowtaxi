#!/bin/bash

# add source roots to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/.."

python3 scripts/partitioner.py
