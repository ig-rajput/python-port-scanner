import socket
import threading
import argparse
import sys
from datetime import datetime

parser = argparse.ArgumentParser(description="Multi-threaded TCP Port Scanner")

parser.add_argument("target", help="Target IP address")
parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout in seconds (default: 1.0)")

args = parser.parse_args()

target = args.target
start_port = args.start
end_port = args.end
timeout = args.timeout

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("[-] Invalid port range. Ports must be between 1 and 65535.")
    sys.exit()

print("=" * 50)
print(f"Target        : {target}")
print(f"Port Range    : {start_port} - {end_port}")
print(f"Timeout       : {timeout} seconds")
print(f"Scan Started  : {datetime.now()}")
print("=" * 50)

open_ports = []
lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))

        if result == 0:
            with lock:
                open_ports.append(port)
                print(f"[OPEN]  Port {port}")

        sock.close()

    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("[-] Could not connect to server.")
        sys.exit()

    except Exception as e:
        print(f"[-] Unexpected error on port {port}: {e}")

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("=" * 50)
print(f"Scan Completed: {datetime.now()}")
print(f"Total Open Ports: {len(open_ports)}")

if open_ports:
    print("Open Ports:", ", ".join(map(str, open_ports)))
else:
    print("No open ports found.")
print("=" * 50)
