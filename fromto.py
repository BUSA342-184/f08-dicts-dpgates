#!/usr/bin/env python3 
"""
This program reads a file and parses out user names and FQDN to a csv list.
"""
import sys
import csv
# creats dictionary to be parsed 
f_u, t_u, f_h, t_h = {}, {}, {}, {}
# opens the file  
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:' ) or line.startswith('To:' ):
        # this splits the lines 
        words = line.split()
        # this splits out the email addresses
        email = words[1]
        # this splits the email addresses into user names and the domain name. 
        usr, hst = email.split('@')
        # this addes the user name and hosts to the dict.
        if line.startswith('From:'):
            f_u[usr] = f_u.get(usr, 0) + 1
            f_h[hst] = f_h.get(hst, 0) + 1
        else:
           t_u[usr] = t_u.get(usr, 0) + 1
           t_h[hst] = t_h.get(hst, 0) + 1 
# this creats the csv list 
cw = csv.writer(sys.stdout)
# this prits out the csv list 
print('--- FROM USER ---')
cw.writerows(sorted(f_u.items()))
print('--- FROM HOST ---')
cw.writerows(sorted(f_h.items()))
print('--- TO USER ---')
cw.writerows(sorted(t_u.items()))
print('--- TO HOST ---')
cw.writerows(sorted(t_h.items()))
        

        