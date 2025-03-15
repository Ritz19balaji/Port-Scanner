import socket
import threading

open_ports = []  # List to store open ports

def scan_port(ip, port):
    """Attempts to connect to a given port on the specified IP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)  # Store open ports
    except Exception as e:
        pass  # Ignore errors for smoother execution

def main():
    target_ip = input("Enter target IP: ")
    ports = range(1, 1025)  # Scans ports 1 to 1024

    print(f"Scanning {target_ip}...\n")
    threads = []

    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Display open ports after scanning
    if open_ports:
        print("\nOpen Ports:")
        for port in sorted(open_ports):
            print(f"[+] Port {port} is open")
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    main()
