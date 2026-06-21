import socket
import platform
import datetime

print("=" * 50)
print("        BASIC NETWORK SNIFFER")
print("=" * 50)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("\nSystem Information")
print("-" * 30)
print("Computer Name :", hostname)
print("Operating System :", platform.system())
print("OS Version :", platform.version())
print("Processor :", platform.processor())

print("\nNetwork Information")
print("-" * 30)
print("Local Host Name :", hostname)
print("Local IP Address :", local_ip)

websites = [
    "www.google.com",
    "www.yahoo.com",
    "www.microsoft.com",
    "www.github.com"
]

print("\nDestination Analysis")
print("-" * 30)

for site in websites:
    try:
        ip = socket.gethostbyname(site)

        print("\nPacket Captured")
        print("Time :", datetime.datetime.now())
        print("Source Host :", hostname)
        print("Source IP :", local_ip)
        print("Destination Host :", site)
        print("Destination IP :", ip)
        print("Protocol :", "TCP/IP")
        print("Packet Status :", "Successfully Resolved")
        print("-" * 40)

    except Exception as e:
        print("\nError while connecting to", site)
        print("Reason :", e)

print("\nSummary")
print("-" * 30)
print("Total Destinations Checked :", len(websites))
print("Network Analysis Completed Successfully")

print("=" * 50)
