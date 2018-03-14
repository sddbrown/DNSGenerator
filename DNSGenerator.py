#
# Tool for creating DNS traffic to test Safe Networking
__author__ = 'Kevin Walsh'

import socket

# Some counters
counter = 0
good_domains = 0
bad_domains = 0
sinkhole_domains = 0
Sinkhole_addr = '72.5.65.111'
file = 'AV_2547.txt'


# Input file.  This code reads domain names from a .txt file and will
# attempt to resolve the IP Addr of the domain
with open(file, 'r') as f:
    # Procssing of the file
    for line in f:
        counter += 1
        try:
            addr1 = line.strip()
            addr2 = socket.gethostbyname(addr1)
            print('{}: {}: {}'.format(counter, addr1, addr2))
            if (addr2 == Sinkhole_addr):
              sinkhole_domains += 1
            good_domains += 1

        except socket.gaierror:
            print('{}: Cannot resolve hostname {}'.format(counter, line))
            bad_domains += 1

# Wrap up
print('Finished!')
print('Total Domains tried:', counter)
print('Domains resolved:', good_domains)
print('Blocked domains:', bad_domains)
print('Sinkhole domains: ', sinkhole_domains)
