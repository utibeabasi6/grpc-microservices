#!/bin/sh

current_dir=`(pwd)`
export KUBECONFIG="${current_dir}/config/grpc-cluster-kubeconfig.yaml"
cd terraform && terraform output --raw lke_kubeconfig  | base64 -D > "${current_dir}/config/grpc-cluster-kubeconfig.yaml"
chmod 400 $KUBECONFIG
	