# kiwi-cloud
Kiwi cloud summer camp challenge

## Build & Push Docker image
The `app` folder contains a simple Python Flask application that returns a JSON output on port `8080`. Also, it is configured with a `/healthcheck` enpoint that returns a 200 response when hit.

To build the Docker image with the Python Flask application, follow these steps:
_Note:_ The instructions should be executed from root folder, with the Dockerfile present
1. Build the Docker image
`docker build -t python-flask-app .`
2. Tag the image
`docker tag python-flask-app pixelpotato/python_flask:${app_version}`
3. Push the image to the Docker registry
`docker push pixelpotato/python_flask:${app_version}`

## Create GKE cluster
This section will describe how to create the GKE cluster using Terraform. 
It is assumed that the user has the service account keys to interact with GCP APIs and that the Kubernetes API is enabled.

_Note:_ The instructions should be executed from `infrastructure` folder
1. Initialise configuration with `terraform init`
2. See Terraform plan with `terraform plan`
3. Apply Terraform changes `terraform apply`

## Connect to the cluster
To conect to the GKE cluster via CLI run thr following command:

`gcloud beta container clusters get-credentials k8s-kiwi --region europe-west1 --project ${project_ID`

_Note:_ `k8s-kiwi` is the cluster name, this can be found in the Terraform configuration for the cluster creation

## Application deployment to the cluster
This section will describe the steps to deploy the Python Flask application to the Kubernetes cluster.
_Note:_ The instructions should be executed from `k8s_app` folder

1. Once connected to the cluster, deploy the application to the cluster using `kubectl apply   -f . `

This will create a Python Flask application with 3 replicase and a service which will expose the application on port 8080.

Also, the application is configured with liveness and readiness probes on `/healthcheck` endpoint.
