---
title: "Data Hackathons App"
description: "simplified self-hostable kaggle-like app"
date: 2023-10-01T12:24:07+01:00
image: "cover.png"
draft: false
---

# Data Hackathons WebApp
As a weekend project, I created a simple fast-api based app which can 
be self-hosted were users can:
- be automatically identified through the auth mechanism (currently azure ad on azure webapp supported)
- browse all published competitions, with their tags
- see a competition page with:
  - a description of the competition and the evaluation metric
  - links to the training data
  - links to the evaluation dataset and the submission template
  - submission form
  - leaderboard of previous submissions with score and submission count.
