.PHONY: grpc
grpc:
	@python3 -m grpc_tools.protoc -I app/grpc/protos --python_out=app/grpc/src --grpc_python_out=app/grpc/src app/grpc/protos/*.proto


.PHONY: build
build:
	@docker compose build

.PHONY: up
up:
	@docker compose up

.PHONY: build-no-cache
build-no-cache:
	@docker compose build --no-cache