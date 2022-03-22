# gRPC microservices with Python

This repository contains the code for three microservices that communicate via gRPC

## Prerequisites

To follow along with this guide, you need to have the following installed

If you are running this with Docker compose, you need to install the following:
- Docker
- Docker compose

If you are deploying to LKE(Linode Kubernetes Engine), you need to have the following setup:
- Linode cli
- Terraform
- A linode account
- Kubectl
- helm

If you are deploying to a local kubernetes cluster, you need to have the following setup:
- Kubectl
- Minikube
- helm

# Deployment

## Via Docker compose
- Clone the repository by running the command `git clone https://github.com/grpc-microservices`
- Run the command `make compose` to start up all the docker-compose services
- Visit `http://localhost:5000` in the browser to view the application. Currently, only 2 routes are available, `/products` to view product information from the database, and `/videos` to view video information from the database.
- Finally stop the running services with `CTRL + C` and run `docker-compose down` to kill the containers.

## Via minikube
- Clone the repository by running the command `git clone https://github.com/grpc-microservices`
- `cd` into the `grpc-microservices` directory
- Run the command `make k8s` to package the helm chart and install the chart into your local minikube cluster.
- Run the command `kubectl get pods` and wait till all the pods are in the `Running` state
- Run the command `minikube service grpc-app-svc` to get a public ip you can use to view the application. Navigate to port 5000 to view the running application. Currently, only 2 routes are available, `/products` to view product information from the database, and `/videos` to view video information from the database.

## Via LKE(Linode Kubernetes Engine)
- Create a personal access token on your linode console
- In the terraform directory, create a file called `terraform.tfvars`
- Write `linode_token = <your_linode_token>` into the `terraform.tfvars file
- Run the command `make init` to initialize terraform and run `make up` setup the linode cluster. On the liode console, make sure the nodes are provisioned before continuing
- Run the command `make kubeconfig` to generate a kubeconfig file that allows you to run kubectl commands against the newly provisioned cluster.
- Run the command `make k8s` to package the helm chart and install the chart into your local minikube cluster.
- Run the command `kubectl get pods` and wait till all the pods are in the `Running` state
- Run the command `kubectl get svc grpc-app-svc` and copy the external ip. Navigate to `external-ip:5000` to view the running application. Currently, only 2 routes are available, `/products` to view product information from the database, and `/videos` to view video information from the database.