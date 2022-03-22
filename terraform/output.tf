output "lke_kubeconfig" {
    value = linode_lke_cluster.grpc-cluster.kubeconfig
    sensitive = true
}