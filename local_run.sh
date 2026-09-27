#!/bin/bash

# Prepare
echo "Preparing content..."
## Generate blog/authors.yml
python generate_authors.py --source config.yml --destination site/blog/authors.yml

# Host site
echo "Starting site..."
cd site
npm run start -- --no-open
