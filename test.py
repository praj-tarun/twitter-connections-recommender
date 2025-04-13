import socket
sock = socket.create_connection(("localhost", 9092), timeout=5)
print("Kafka is reachable")
