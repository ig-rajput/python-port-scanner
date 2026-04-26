# Python Port Scanner
# Built for learning TCP port scanning using sockets

# Future improvement:
# use thread pool instead of creating one thread per port

import socket
import threading
import argparse
import sys
import time
from datetime import datetime


common_ports = {
    21:"FTP",
    22:"SSH",
    23:"Telnet",
    25:"SMTP",
    53:"DNS",
    80:"HTTP",
    110:"POP3",
    443:"HTTPS"
}


open_ports = []
lock = threading.Lock()


def scan_port(target, port, timeout):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target,port))

        if result == 0:

            service = common_ports.get(port,"Unknown")

            with lock:
                open_ports.append(port)
                print(f"[OPEN] Port {port} ({service})")

        sock.close()


    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        print("Connection error")
        sys.exit()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Simple Multi-threaded TCP Port Scanner"
    )

    parser.add_argument(
        "target",
        help="Target IP address"
    )

    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="Start port"
    )

    parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=1024,
        help="End port"
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=1.0,
        help="Timeout"
    )

    args = parser.parse_args()


    if args.start < 1 or args.end > 65535 or args.start > args.end:
        print("Invalid port range")
        sys.exit()


    print("\nPython Port Scanner")
    print("="*45)
    print("Target       :",args.target)
    print("Port Range   :",args.start,"-",args.end)
    print("Timeout      :",args.timeout)
    print("Started      :",datetime.now())
    print("="*45)


    start_time = time.time()

    threads = []


    for port in range(args.start,args.end+1):

        thread = threading.Thread(
            target=scan_port,
            args=(args.target,port,args.timeout)
        )

        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()


    end_time = time.time()


    print("\n"+"="*45)
    print("Scan Complete")
    print("Finished     :",datetime.now())
    print("Open Ports   :",len(open_ports))

    if open_ports:
        print("Port List    :",",".join(map(str,open_ports)))
    else:
        print("No open ports found")

    print("Scan Time    :",round(end_time-start_time,2),"seconds")
    print("="*45)