Python Port Scanner

Overview

This project is a multi-threaded TCP port scanner built using Python.
It scans a target host within a given port range and identifies which ports are open.
The goal of this project was to understand how TCP connections work at a low level and how basic network scanning tools operate behind the scenes
Why I Built This
Instead of just using tools like Nmap, I wanted to understand how port scanning actually works.
This project helped me learn how TCP handshakes, sockets, and threading function in real-world scenarios.
Features
Scan any target IP address
Custom port range selection
Adjustable timeout
Multi-threaded scanning for faster performance
Displays total open ports found
Clean and structured output
Technologies Used
Python
socket module
threading module
argparse (for command-line arguments)

How to Run

Basic scan (default ports 1–1024):

python scanner.py 127.0.0.1
Custom port range:

python scanner.py 127.0.0.1 -s 1 -e 100
With custom timeout:

python scanner.py 127.0.0.1 -s 1 -e 100 -t 0.5
Sample Output

==================================================
Target        : 127.0.0.1
Port Range    : 1 - 100
Timeout       : 1.0 seconds
Scan Started  : 2026-02-13 12:34:56
==================================================
[OPEN]  Port 22
[OPEN]  Port 80
==================================================
Scan Completed: 2026-02-13 12:35:02
Total Open Ports: 2
Open Ports: 22, 80
==================================================
What I Learned
How TCP socket connections work
Difference between open and closed ports
Using connect_ex() for safe connection handling
Multi-threading to improve performance
Designing a simple CLI-based security tool
