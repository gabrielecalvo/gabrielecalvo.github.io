---
author: "Gabe Calvo"
title: "Docker Data Analysis Image"
date: "2019-03-05"
description: "A custom made data analysis Docker Image with JupyterLab and main python data analysis libraries."
image: "cover.png"
# categories:
#   - "Coding"
tags:
  - "docker"
  - "data science"
draft: false
---

I worked on a demo image to have jupyterlab working inside docker and accessible from the host machine.

The documentation and usage is detailed [**_here_**](https://github.com/gabrielecalvo/dataanalysis-jupyterlab).

But I'd like to take a moment to summerise some pros of this solution:

1. It allows a **standardised** development environment.
2. It ensure any analysis performed in it is fully **repeatable**.
3. It runs on pretty much **any machine** that runs docker.
4. If you screw things up, **you can delete the container and start from a brand new one**. To keep data you just need to mount a volume (as explained in the documentation).
5. You can **install libraries that only run on linux**.
