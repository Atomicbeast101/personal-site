#!/bin/bash

# Cleanup
rm -rf .venv

# Setup
python3 -m venv .venv
.venv/bin/pip install -r resume/requirements.txt
.venv/bin/pip install -r site/requirements.txt
