import time
import grpc
import order_pb2
import order_pb2_grpc

print("Sending sample payload")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update with payload
order = order_pb2.OrderMessage(
    id="001",
    created_by="John Smith",
    status=order_pb2.OrderMessage.Status.PROCESSING,
    created_at="2023-01-30",
    equipment=[order_pb2.OrderMessage.Equipment.MONITOR,
               order_pb2.OrderMessage.Equipment.WEBCAM, ],
)

response = stub.Create(order)
