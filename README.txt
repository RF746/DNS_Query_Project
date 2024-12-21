# DNS Query Tool

## Overview

The **DNS Query Tool** is a Python-based project that sends a custom DNS query to a specified DNS server and retrieves the resolved IP address for a given domain. This tool demonstrates the practical application of low-level networking concepts and the Domain Name System (DNS) protocol.

---

## Features

- **Custom DNS Query**: Constructs and sends a DNS query to a specified server.
- **UDP Socket Communication**: Uses Python's `socket` module for networking.
- **DNS Response Parsing**: Extracts and displays the IP address from the DNS server's response.
- **User-Friendly**: Accepts user input for the domain name and displays results clearly.

---

## How It Works

1. **DNS Query Construction**:
   - Builds a DNS query packet using the DNS protocol's standard format.
   - Encodes the domain name as required by the protocol.

2. **Communication**:
   - Sends the query to a DNS server (default: Google DNS `8.8.8.8`) over UDP.
   - Receives and parses the server's response.

3. **Result Display**:
   - Extracts the IP address from the DNS response and displays it to the user.

---

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of networking and DNS concepts (optional).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/dns-query-tool.git
   cd dns-query-tool
