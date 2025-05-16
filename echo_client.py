import grpc
import echo_pb2
import echo_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = echo_pb2_grpc.EchoServiceStub(channel)
        response = stub.EchoMessage(echo_pb2.EchoRequest(message="Hi Simple Echo Project!"))
        print("Response from server:", response.echoed_message)

if __name__ == '__main__':
    run()
