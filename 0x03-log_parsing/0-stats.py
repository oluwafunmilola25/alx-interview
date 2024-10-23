#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys

#dictionary to store counts of each status code
status_codes_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

def print_stats():
    """Prints the total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")
        
        def signal_handler(sig, frame):
    """Handle keyboard interrupt (CTRL + C) to print the stats before exiting."""
    print_stats()
    sys.exit(0)
    
    # Register the signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)
    # Read input line by line from stdin
for line in sys.stdin:
    try:
        # Example line format: '123.45.67.89 - [01/Jan/2023:10:15:20] "GET /projects/260 HTTP/1.1" 200 512'
        parts = line.split()

        # Ensure the input matches the expected format
        if len(parts) < 7:
            continue
        
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        total_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        # After every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats()
    except (ValueError, IndexError):
        # Skip lines that don't match the expected format
        continue

# In case the loop ends without a keyboard interruption, print the final stats
print_stats()