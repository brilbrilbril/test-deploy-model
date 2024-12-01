DOCUMENTATION

This project's purpose is to apply CI/CD Generative Model using Google Cloud and Kubernetes

1. Define dependencies needed here
   This project is using gpt2 as model, so we need to insert torch and transformers
   To build API endpoint and server gateaway, the high-performance web framework like fastAPI and uvicorn
   store the dependencies name in requirement.txt and it will be like this
   ![image](https://github.com/user-attachments/assets/159e9aea-fb22-4f36-ae14-510a99dd2e85)

2. Define dockerfile contains the workdir, copied requirements.txt and app to workdir path, command to install dependencies, and command to run the uvicorn
3. Define .yaml file to do deployment and service in Kubernetes
4. Make a trigger on google cloud build
   The goal is to trigger google cloud build, executing file cloudbuild.yaml everytime there is a commit changes in github
   ![image](https://github.com/user-attachments/assets/9934520b-09ab-4007-bfc0-5e7ea207d8ed)
5. Define cloudbuild.yaml
   This contains step to build images using docker image prebuild by google (gcr), push the image, authenticate the project, and deploy to the image to Kubernetes
6. Define main app contains fastapi framework, the function that will be executed via route, initialized generation model, and function to do text generation
7. To test the model, there is a test.py that access the external IP provided by Kubernetes service and make a POST request to fastAPI endpoint to do text generation
