#!/bin/sh

# Generate products schema
python3 -m grpc.tools.protoc -Iproducts --python_out=main --grpc_python_out=main products/products.proto
cp main/products*.py products


# Generate videos schema
python3 -m grpc.tools.protoc -Ivideos --python_out=main --grpc_python_out=main videos/videos.proto
cp main/videos*.py videos
