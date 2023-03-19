import socket

# Define the IP and port of the source and destination addresses
src_ip = '192.168.1.100'
src_port = 80
dst_ip = '192.168.1.200'
dst_port = 8080

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# Receive incoming packets
while True:
    packet = s.recv(4096)

    # Extract the source and destination addresses from the packet
    src, dst, *_ = packet[:20].unpack('!4s4s2s2s')

    # Check if the source and destination addresses match the defined addresses
    if src.decode() == src_ip and dst.decode() == dst_ip:
        # Extract the source and destination ports from the packet
        src_p, dst_p, *_ = packet[20:].unpack('!2s2s')
        src_p, dst_p = int.from_bytes(src_p, 'big'), int.from_bytes(dst_p, 'big')

        # Check if the source and destination ports match the defined ports
        if src_p == src_port and dst_p == dst_port:
            print(f'Accepted packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}')
        else:
            print(f'Rejected packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}')
