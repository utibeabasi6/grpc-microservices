resource "linode_lke_cluster" "grpc-cluster" {
    label       = "grpc-cluster"
    k8s_version = "1.22"
    region      = "us-southeast"
    tags        = ["grpc"]

    pool {
        type  = "g6-standard-2"
        count = 3
    }
}