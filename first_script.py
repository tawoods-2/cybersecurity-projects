#First cybersecurity practice script

target = "192.168.1.1"

print("Scanning target:", target)

for port in range(1,101):
    print(f"Checking port {port}...")