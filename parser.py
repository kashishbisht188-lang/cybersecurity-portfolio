import sys
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description="Failed Login Parser")
parser.add_argument("--file", help="Path to log file (optional)")
args = parser.parse_args()

ip_list = []

if args.file:
    try:
        with open(args.file) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        exit()
else:
    lines = sys.stdin.readlines()

for line in lines:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[10]
        ip_list.append(ip)

ip_counts = Counter(ip_list)

print("\nTop Failed Login Attempts:")
print("-" * 30)
for ip, count in ip_counts.most_common(10):
    print(f"{ip:<20} {count} attempts")

