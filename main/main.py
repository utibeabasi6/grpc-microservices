from flask import Flask
import products_pb2
import products_pb2_grpc
import videos_pb2
import grpc
import videos_pb2_grpc

app = Flask(__name__)

@app.route("/products")
def getProducts():
    products = []
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = products_pb2_grpc.ProductsStub(channel)
        for response in stub.GetProducts(products_pb2.ProductRequest()):
            products.append({"name": response.name, "price": response.price, "image": response.image})
    
    return {"itemCount": len(products), "items": products}

@app.route("/videos")
def getVideos():
    videos = []
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = videos_pb2_grpc.VideosStub(channel)  
        for response in stub.GetVideos(videos_pb2.VideoRequest()):
            videos.append({"url": response.url})
    return {"itemCount": len(videos), "items": videos}

if __name__ == "__main__":
    app.run(debug=True)