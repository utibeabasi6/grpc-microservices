import videos_pb2
import videos_pb2_grpc
from concurrent import futures
import logging
import sqlite3
import grpc

class Videos(videos_pb2_grpc.VideosServicer):
    def GetVideos(self, request, context):
        conn = sqlite3.connect("videos.db")
        rows = conn.execute("SELECT * from videos").fetchall()
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