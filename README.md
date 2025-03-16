# Gabe's Blog

This repo contains the code that generate the static site of my blog: https://gabrielecalvo.github.io/

## Useful local commands
```bash
# create a new post
hugo new content/post/$POSTNAME/index.md

# run local server (with rebuild)
hugo server -D --disableFastRender

# updating the theme (as submodule)
hugo mod get -u github.com/CaiJimmy/hugo-theme-stack/v3
hugo mod tidy
```