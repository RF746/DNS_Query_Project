import socket
import struct

def build_dns_query(domain):
    """Build a DNS query for the given domain."""
    # Header: Transaction ID (2 bytes), Flags (2 bytes), Questions (2 bytes), Answer RRs (2 bytes), Authority RRs (2 bytes), Additional RRs (2 bytes)
    transaction_id = 0x1234  # Random transaction ID
    flags = 0x0100          # Standard query with recursion
    questions = 1
    answer_rrs = 0
    authority_rrs = 0
    additional_rrs = 0

    header = struct.pack(">HHHHHH", transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs)

    # Question: Domain Name, Type (2 bytes), Class (2 bytes)
    domain_parts = domain.split(".")
    question = b""
    for part in domain_parts:
        question += struct.pack("B", len(part)) + part.encode()
    question += b"\x00"  # End of domain name
    question += struct.pack(">HH", 1, 1)  # Type A, Class IN

    return header + question


def parse_dns_response(response):
    """Parse the DNS response and extract the IP address."""
    header = response[:12]  # First 12 bytes are the header
    question = response[12:]  # The question starts here

    # Skip the question section (variable length)
    pointer = question.find(b"\x00") + 5

    # Extract the answer section
    answer = question[pointer:]

    # Get the IP address from the answer section
    if len(answer) > 16:  # Check if there's an answer
        ip_parts = struct.unpack(">BBBB", answer[-4:])
        return f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3]}"
    else:
        return "No IP address found in the response."


def dns_query(domain, dns_server="8.8.8.8", port=53):
    """Send a DNS query to a DNS server."""
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)

    try:
        # Build the DNS query
        query = build_dns_query(domain)

        # Send the query to the DNS server
        print(f"Sending DNS query for {domain} to {dns_server}...")
        client_socket.sendto(query, (dns_server, port))

        # Receive the response
        response, _ = client_socket.recvfrom(512)
        print("DNS response received!")

        # Parse and return the IP address
        ip_address = parse_dns_response(response)
        return ip_address

    except socket.timeout:
        return "Request timed out."
    finally:
        client_socket.close()


if __name__ == "__main__":
    # Get domain input from the user
    domain = input("Enter the domain name (e.g., example.com): ")
    ip_address = dns_query(domain)
    print(f"IP address for {domain}: {ip_address}")
