import videos_pb2
import videos_pb2_grpc
from concurrent import futures
import logging
import grpc
import psycopg2
import os

class Videos(videos_pb2_grpc.VideosServicer):
    def GetVideos(self, request, context):
        conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_URL"),
        user="postgres",
        password=os.environ.get("POSTGRES_PASSWORD"))
        cursor = conn.cursor()
        cursor.execute("SELECT * from videos")
        rows = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        for video in rows:
            yield videos_pb2.Video(url=video[0])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    videos_pb2_grpc.add_VideosServicer_to_server(Videos(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()