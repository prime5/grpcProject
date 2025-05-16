import grpc
from concurrent import futures
import echo_pb2
import echo_pb2_grpc

class EchoService(echo_pb2_grpc.EchoServiceServicer):
    def EchoMessage(self, request, context):
        return echo_pb2.EchoResponse(echoed_message=f"Echo: {request.message}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServiceServicer_to_server(EchoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
