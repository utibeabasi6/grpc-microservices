up:
	@cd terraform && terraform apply --auto-approve

down:
	@cd terraform && terraform destroy --auto-approve


build:
	@chmod +x scripts/gen.sh && ./scripts/gen.sh

k8s: 
	# @chmod +x scripts/ingress.sh && ./scripts/ingress.sh
	@cd helm && helm package . && helm install grpc ./helm-0.1.0.tgz

compose:
	@docker-compose up

init:
	@cd terraform && terraform init

kubeconfig:
	@chmod +x scripts/kubeconfig.sh && ./scripts/kubeconfig.sh

upgrade:
	@cd helm && helm package . && helm upgrade grpc ./helm-0.1.0.tgz
