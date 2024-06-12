---
author: "Gabe Calvo"
title: "tENVplate"
date: "2024-05-20"
description: "I built a tool to simplify .env template filling"
image: "cover.jpg"
# categories:
#   - "Coding"
tags:
  - "secrets"
  - "python"
  - "key-vault"
draft: false
---

# tENVplate: a simple .env template filler
When cloning a project I often found it annoying that, even if a `.env.template` file is available, one still needs to ask for a "filled" version or chase down the values of the secrets on your own.

Wouldn't it be easier to create the template with a reference to the vault service used to store the secrets?

Last weekend I managed to create a simple tool that tries to address that pain point for anyone currently using azure keyvault or k8s.

Hope people find it as useful as I do: 
https://github.com/gabrielecalvo/tenvplate