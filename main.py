import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc


class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Get(self, request, context):
        order_one = order_pb2.OrderMessage(
            id="001",
            created_by="John Smith",
            status=order_pb2.OrderMessage.Status.PROCESSING,
            created_at="2023-01-15",
            equipment=[order_pb2.OrderMessage.Equipment.MONITOR]
        )

        order_two = order_pb2.OrderMessage(
            id="002",
            created_by="Major Jeff",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at="2023-01-30",
            equipment=[order_pb2.OrderMessage.Equipment.MOUSE]
        )

        res = order_pb2.OrderMessageList()
        res.orders.extend([order_one, order_two])
        return res

    def Create(self, request, context):
        print("Message Received!")

        request_value = {
            "id": request.id,
            "created_by": request.created_by,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": ["MONITOR"],
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
