FROM python:3.11.7-slim

ARG GRPC_PROTOBUF_PATH=./app/grpc/protos
ARG GRPC_OUT_PATH=./app/grpc/src

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --user -r ./requirements.txt
RUN python -m pip install -U watchdog

COPY --chown=app:app . ./

# RUN echo "export PATH=$PATH" > /etc/environment

# RUN if [ "${PROJECT_ENVIROMENT}" != "development" ]; then \
#     python \
#         -m grpc_tools.protoc \
#         -I ${GRPC_PROTOBUF_PATH} \
#         --python_out=${GRPC_OUT_PATH} \
#         --grpc_python_out=${GRPC_OUT_PATH} \
#         ${GRPC_PROTOBUF_PATH}/*.proto; \
#     fi
