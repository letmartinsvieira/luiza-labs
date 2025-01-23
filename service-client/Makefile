# GRPC var
GRPC_OUT_PATH=app/grpc/src
GRPC_PROTOBUF_PATH=app/grpc/protos
GRPC_PROTOBUFF_JS_PATH=app/grpc/js

SERVICE=service-client
ROOT=$(shell pwd)
DOCKER_NODE_PROTO_PKG=grpc/node:0.11-onbuild
NETWORK_NAME=luiza-labs-test
NETWORK_ID=$(shell docker network ls -qf "name=${NETWORK_NAME}")
COMPOSE_HTTP_TIMEOUT=300

# Bulding arguments
OS_NAME=$(shell uname)
USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)
BUILD_ARG=--build-arg USER_ID=${USER_ID} --build-arg GROUP_ID=${GROUP_ID}

DB_NETWORK=luiza-labs-test
DB_PASS=postgres
DB_HOST=svc_client_postgres
DB_NAME=service_client_db
DB_USER=postgres
DOCKER_POSTGRES_CLIENT_IMAGE=postgres:15-alpine
DB_PATH=app/database/orm_config
DB_MIGRATIONS_PATH=app/database/migrations

.PHONY: build
build:
	@docker compose build --no-cache --pull ${BUILD_ARG}

.PHONY: grpc
grpc:
	@if [ -n "${proto}" ]; then \
		$(eval proto:=*) \
		:; \
	fi; \

	@docker compose run --rm ${SERVICE} python -m grpc_tools.protoc -I ${GRPC_PROTOBUF_PATH} --python_out=${GRPC_OUT_PATH} --grpc_python_out=${GRPC_OUT_PATH} ${GRPC_PROTOBUF_PATH}/${proto}.proto
	

.PHONY: protos
protos:
	@python3 -m grpc_tools.protoc -I app/grpc/protos --python_out=app/grpc/src --grpc_python_out=app/grpc/src app/grpc/protos/*.proto

.PHONY: init
init:
	@if [ -n '${NETWORK_ID}' ]; then \
		echo '${NETWORK_NAME} already exists'; \
	else \
		docker network create -d bridge ${NETWORK_NAME}; \
	fi \

.PHONY: db
db:
	@docker compose up -d postgres

#.PHONY: db-init
#db-init:
#	@docker run --rm -it --net=${DB_NETWORK} svc_client_postgres -c \
#		"if ! PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -U ${DB_USER} -lqt | cut -d \| -f 1 | grep -qw ${DB_NAME}; then \
#			PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -U ${DB_USER} -c 'CREATE DATABASE service_client_db'; \
#		fi"

.PHONY: db-create
db-create:
	# Check if database already exists...
	@docker run --rm -it --net=${DB_NETWORK} ${DOCKER_POSTGRES_CLIENT_IMAGE} sh -c \
		"if ! PGPASSWORD=${DB_PASS} psql -h ${DB_HOST} -U ${DB_USER} -lqt | cut -d \| -f 1 | grep -qw ${DB_NAME}; then \
			PGPASSWORD=${DB_PASS} psql -h ${DB_HOST} -U ${DB_USER} -c 'CREATE DATABASE ${DB_NAME}'; \
		fi"

.PHONY: db-shell
db-shell:
	@docker run --rm -it --net=${DB_NETWORK} ${DOCKER_POSTGRES_CLIENT_IMAGE} sh -c "PGPASSWORD=${DB_PASS} psql -h ${DB_HOST} -U ${DB_USER} ${DB_NAME}"

.PHONY: db-drop
db-drop:
	@docker run --rm -it --net=${DB_NETWORK} ${DOCKER_POSTGRES_CLIENT_IMAGE} sh -c "PGPASSWORD=${DB_PASS} psql -h ${DB_HOST} -U ${DB_USER} -c 'DROP DATABASE IF EXISTS ${DB_NAME}'"

.PHONY: up
up:
	@docker compose up -d

.PHONY: db-migrate
db-migrate:
	@echo Migrating development db
	@docker compose run --rm ${SERVICE} orator migrate sh -c ${DB_PATH}/orator_config.py -p ${DB_MIGRATIONS_PATH} -n --force
	@echo Finishing migrations

.PHONY: db-migration-create
db-migration-create:
	@docker compose run --rm -i -t ${SERVICE} orator migrations:make create_users_table