#This program is written for both standard as well as extended ACL. And it can work
#on any number of ACL's and Addresses. If no ACL rule matches with an address then by
#default it is denied, as per the rules of ACL.

import re

with open("Path to list_of_packets.txt","r") as f:
          for line in f:
               line = line.replace("\n", "")
               ip_chunks = line.split(" ")
               packet_source_ip_parts=ip_chunks[0].split(".")
               packet_destination_ip_parts=ip_chunks[1].split(".")
               flag=0
               acl = open("Path to ACL.txt", "r")
               for line in acl:
                   if re.match("access-list", line):
                       line = line.replace("\n", "")
                       acl_chunks = line.split(" ")
                       if(len(acl_chunks)<=5):
                           acl_source_ip_parts=acl_chunks[3].split(".")
                           source_mask_parts=acl_chunks[4].split(".")
                           for i in range(4):
                               if(source_mask_parts[i]=='255'):
                                   acl_source_ip_parts[i]='0'
                           m=0
                           for j in range(4):
                               if(acl_source_ip_parts[j]=='0'):
                                   m=m+1
                               elif(acl_source_ip_parts[j]==packet_source_ip_parts[j]):
                                   m=m+1
                           if(m==4):
                               print ip_chunks[0]+' '+ip_chunks[1]+' '+acl_chunks[2]
                               flag=1
                               break
                       else:
                           acl_source_ip_parts=acl_chunks[4].split(".")
                           source_mask_parts=acl_chunks[5].split(".")
                           acl_destination_ip_parts=acl_chunks[6].split(".")
                           destination_mask_parts=acl_chunks[7].split(".")
                           for k in range(4):
                               if(source_mask_parts[k]=='255'):
                                   acl_source_ip_parts[k]='0'
                           
                           for l in range(4):
                               if(destination_mask_parts[l]=='255'):
                                   acl_destination_ip_parts[l]='0'
                       
                           n=0
                           for p in range(4):
                               if(acl_source_ip_parts[p]=='0'):
                                   n=n+1
                               elif(acl_source_ip_parts[p]==packet_source_ip_parts[p]):
                                   n=n+1
                                   
                           for q in range(4):
                               if(acl_destination_ip_parts[q]=='0'):
                                   n=n+1
                               elif(acl_destination_ip_parts[q]==packet_destination_ip_parts[q]):
                                   n=n+1
                                   
                           if(n==8):
                               print ip_chunks[0]+' '+ip_chunks[1]+' '+acl_chunks[2]
                               flag=1
                               break
                           
               if(flag==0):
                   print ip_chunks[0]+' '+ip_chunks[1]+' deny'

f.close()
acl.close()