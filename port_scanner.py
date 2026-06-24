print("=== PORT SCANNER V1 ===")
import socket

target = input("Enter a target")

print = ("Starting scan on", target)

for port in range (1,11):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.socksettimeout(1)
    
    result = sock.connect_ex((target, port))
    
    if result == 0
    print("Port", port, "is OPEN")
    else:
    print("Port", port, "is CLOSED")
    
    sock.close()
    
print("Scan complete")