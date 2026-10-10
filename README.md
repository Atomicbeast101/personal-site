# Personal Site
Automated personal website and resume generation using YAML, Hugo, RenderCV, and CI/CD pipelines to maintain a single source of truth and streamline builds and deployment.

## Technology

* [Gitea Runner](https://docs.gitea.com/runner/) (CI/CD)
* [RenderCV](https://rendercv.com/)
* [Hugo](https://gohugo.io/) with [hugo-noir](https://github.com/prxshetty/hugo-noir) theme

## Update Guide

1) Make changes to `config.yml` file to apply to both personal site and resume.
2) Run `bash build.sh` to build Python virtual environment if not done before.
3) Run `bash run.sh` to build the resume and website. URL can be accessed here: [http://localhost:1313/](http://localhost:1313/)

## CI/CD Pipeline

TODO_IMAGE_HERE
