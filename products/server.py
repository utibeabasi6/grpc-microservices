import products_pb2
import products_pb2_grpc
from concurrent import futures
import logging
import sqlite3
import grpc
import os
import psycopg2

class Products(products_pb2_grpc.ProductsServicer):
    def GetProducts(self, request, context):
        conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_URL"),
        user="postgres",
        password=os.environ.get("POSTGRES_PASSWORD"))
        cursor = conn.cursor()
        cursor.execute("SELECT * from products")
        rows = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        for product in rows:
            yield products_pb2.Product(name=product[0], image=product[2], price=product[1])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    products_pb2_grpc.add_ProductsServicer_to_server(Products(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()