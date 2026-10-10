#!/bin/bash

# Generate resume
.venv/bin/python resume/convert_to_cv.py --source config.yml --template resume/template.yml --destination resume/generated.yml
.venv/bin/rendercv render resume/generated.yml --pdf-path resume.pdf
cp resume/resume.pdf site/content/resume.pdf

# # Run hugo site
.venv/bin/python site/generate_content.py --source config.yml --destination site/data/en
hugo server -s site
