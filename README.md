# Immo API

![alt text](/assets/download.png)

## Introduction

This scripts allows you to predict prices based on a prediciton model created using data scraped from immo web (for info on that project, visit the following repository : https://github.com/yassbarona/challenge-collecting-data).

## Instalation

In order to install this game proceed with the folowing steps:

  1- Clone the code from the repository in the address https://github.com/yassbarona/immo-api/
  
  2- Open your termial
  
  3- Go to the folder you just cloned from Github
  
  4- If the idea is to run the API locally type the command "uvicorn app:app --reload". To run the API on a web browser go to the link: https://flask-docker-31-03.herokuapp.com/docs

  5- Enjoy!
  
  ## Descritpion
  
  1- This script shows the process of creating an API, creating images an containers using Docker and deploying it on Heroku.
  
  2- The API was initially built using a micro-web framework called Flask. Later on the attemp to have a frieandlier user interface the script was change to use FastAPI as its framework since the prevously mentioned generates automatic interactive API documentation (provided by Swagger UI)

  3- The "dockerization" and deplyment proceses are very standard and stright forward. The challenge consists on adapting the commands in the Dockerfile to the API framework you are using. A better explination of this process can be found on the following repository: https://github.com/becodeorg/BXL-Bouman-4/tree/master/content/5.deployment/4.Web_Application
  
  4- any modification of the pre-set settings can be done directly over the cloned script. For any further request, feel free to contact us at : support@flask-or-fastapi.eth
  
  ## Results
  
  ![alt text](/assets/Screenshot.png)
  
  ### DISCLAMER
  We accept no liabilities for the execution of this code. Stay in school... or not, we don't care.
