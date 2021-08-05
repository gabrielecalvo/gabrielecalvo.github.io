---
author: "Gabe Calvo"
title: "Streamlit on Azure"
date: "2021-05-07"
description: "Guide to deploying Streamlit on Azure App Service."
image: "cover.png"
# categories:
#   - "Coding"
tags:
  - "azure"
  - "streamlit"
draft: false
---

# Guide to Streamlit on Azure

Streamlit is a python library that allows for quick WebApp development for relatively simple applications.
It provides common widgets and simple procedural logic.

In this guide, we will deploy a barebone app that I recommend using as your starting point if you want to 
deploy to Azure App Service.
I have found the deployment to be a little tempremental so I hope this can help you.

I've taken information from [here](https://towardsdatascience.com/deploying-a-streamlit-web-app-with-azure-app-service-1f09a2159743), though that alone did not work for me.
Cloning and deploying [this](https://github.com/MarcSkovMadsen/awesome-streamlit/tree/master/.streamlit) worked, but I then simplified it and updated versions to get this guide.

## Downloading the barebone app
I've prepared all the files you'll need to get a start [here](http://raw.githubusercontent.com/gabrielecalvo/gabrielecalvo.github.io/main/assets/minimal_azure_streamlit.zip)

## Creating Azure Resources
The following resources have to be created:
 - resource group
 - azure container registry
 - app service

You can create basic level of them using the [azure cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) 
as shown below. I will assume you are using bash. I usually prefer setting the variables once and using them in all future commands. The ones you will need are:
```bash
export LOCATION="xxx"
export RESOURCE_GROUP="xxx"
export CONTAINER_REGISTRY="xxx"
export IMAGE_NAME="xxx"
export WEBAPP_NAME="xxx"
export SERVICE_PLAN_NAME="xxx"
```

To see all possible locations use `az account list-locations`

Remember that *WEBAPP_NAME* will go in the url (https://*WEBAPP_NAME*.azurewebsites.net) so it needs to be unique across all azurewebsites.

The resource-creating commands are:
 - resource group: `az group create -l $LOCATION -n $RESOURCE_GROUP`
 - azure container registry: `az acr create --name $CONTAINER_REGISTRY --resource-group $RESOURCE_GROUP --sku basic --admin-enabled true`
 - app service: `az appservice plan create -g $RESOURCE_GROUP -n $SERVICE_PLAN_NAME -l $LOCATION --is-linux --sku B1`

If you get authorisation errors, make sure you are logged in (`az login` and `az acr login -n $CONTAINER_REGISTRY`)

Once those resources are set-up, we move on to building the image (remotely) and creating the web app based on it
```bash
az acr build --registry $CONTAINER_REGISTRY --resource-group $RESOURCE_GROUP --image $IMAGE_NAME .
az webapp create -g $RESOURCE_GROUP -p $SERVICE_PLAN_NAME -n $WEBAPP_NAME -i $CONTAINER_REGISTRY.azurecr.io/$IMAGE_NAME:latest
```


## Local Development
In order to speed up development it is usually better to build and test the image by using docker locally
```bash
# locally build the test image
docker build -t tst .

# test the image locally
docker run --rm -it -p 80:80 tst
```


## Pushing the image to the Container Registry
Pushing the image will trigger an update of the WebApp on the next request.
```bash
# re-tag the image and push it to the repository
docker image tag tst $CONTAINER_REGISTRY.azurecr.io/$IMAGE_NAME:latest
docker push $CONTAINER_REGISTRY.azurecr.io/$IMAGE_NAME:latest
```

The update can be a bit fiddly, so I usually prefer restarting the app from the Azure Web UI to be sure and monitor the Log Stream.


## Futher Considerations
There are a couple of things to bear in mind:
- The way the webapp defaults, it will be available to the internet unless authorisation is specified.
- The Dockerfile is in its simplest form. When opening the website to the internet there are security 
  concerns to address, [here](https://www.youtube.com/watch?v=JE2PJbbpjsM) is a nice overview.
