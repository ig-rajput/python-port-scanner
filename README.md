Python Port Scanner

This is a simple TCP port scanner that I built using Python.
It scans a target IP address and checks which ports are open in a given range.
I made this project to understand how port scanning actually works instead of only using tools like Nmap.
___________________________________________________________________________

What This Project Does

- Takes a target IP as input
- Scans ports in a selected range
- Uses multi-threading to scan faster
- Shows which ports are open
- Displays total open ports at the end
___________________________________________________________________________

Why I Built This

- As a cybersecurity student, I wanted to understand:
- How TCP connections work
- How open and closed ports are detected
- How the socket module works
- How threading improves performance
- This project helped me understand networking concepts in a practical way.
___________________________________________________________________________

Technologies Used

- Python
- socket
- threading
- argparse
- How To Run
- Basic scan:
- Copy code
___________________________________________________________________________

How to Run

Basic scan
python scanner.py 127.0.0.1

Custom port range:
python scanner.py 127.0.0.1 -s 1 -e 100

With timeout:
python scanner.py 127.0.0.1 -s 1 -e 100 -t 0.5

___________________________________________________________________________
Sample Output
___________________________________________________________________________

Target        : 127.0.0.1
Port Range    : 1 - 100
Timeout       : 1.0 seconds

___________________________________________________________________________
[OPEN] Port 22
[OPEN] Port 80
___________________________________________________________________________
Total Open Ports: 2
Open Ports: 22, 80
___________________________________________________________________________

What I Learned From This Project

- Basics of TCP communication
- How connect_ex() works
- Error handling in network programs
- Using command-line arguments
- Writing a simple security tool


