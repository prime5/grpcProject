# 🔁 EchoService – A Simple gRPC Microservice in Python

This project is a lightweight demonstration of a gRPC-based microservice in Python. It features a client-server architecture where the client sends a message, and the server responds by echoing it back with a prefix.

## ✨ Why gRPC?

gRPC is a high-performance, open-source framework designed for internal service-to-service communication. It leverages:
- HTTP/2 for multiplexed, efficient transport
- Protocol Buffers for fast, compact binary serialization
- Auto-generated client/server code from `.proto` files

---

## 📁 Project Structure

grpc_echo_demo/
│
├── echo.proto # Service definition using Protocol Buffers
├── echo_pb2.py # Generated message classes
├── echo_pb2_grpc.py # Generated service classes
├── echo_server.py # Server implementation
└── echo_client.py # Client implementation


---

## 🚀 How to Run This Project

### 1. Clone the Repo & Set Up Environment
```bash
git clone https://github.com/your-username/grpc-echo-demo.git
cd grpc-echo-demo
python3 -m venv venv
source venv/bin/activate
pip install grpcio grpcio-tools

2. Generate gRPC Code
bash
Copy
Edit
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. echo.proto
3. Start the Server
bash
Copy
Edit
python echo_server.py
4. Run the Client
bash
Copy
Edit
python echo_client.py
You should see:

pgsql
Copy
Edit
Response from server: Echo: Hello from client!
