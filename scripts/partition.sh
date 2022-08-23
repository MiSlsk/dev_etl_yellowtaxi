#!/bin/bash

# add source roots to PYTHONPATH so that the scripts can see ./shared modules
export PYTHONPATH="${PYTHONPATH}:$(pwd)/.."

python3 scripts/partitioner.py
