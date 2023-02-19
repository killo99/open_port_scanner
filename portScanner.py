import socket

def scan_ports(host, start_port, end_port):
    """
    Scan for open ports on the specified host between start_port and end_port (inclusive)
    """
    open_ports = []
    for port in range(start_port, end_port+1):
        # Create a new socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout to prevent the socket from blocking forever
        sock.settimeout(1)
        try:
            # Attempt to connect to the specified host and port
            sock.connect((host, port))
            # If the connection is successful, add the port to the list of open ports
            open_ports.append(port)
            # Close the socket
            sock.close()
        except:
            # If the connection attempt fails, just close the socket
            sock.close()
    return open_ports

host = input("Enter target IP: ")
start_port = 1
end_port = 65535
open_ports = scan_ports(host, start_port, end_port)

print(f"Open ports on {host}: {open_ports}")
