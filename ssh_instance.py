#!/usr/bin/env python3

import os
from Ec2 import Ec2
import argparse
from os.path import expanduser

def main(args):
    ec2 = Ec2()
    instance_list = ec2.get_instance_list(["running"])
    ec2.print_instance_list(instance_list)
    host_idx = int(input("Type host id to ssh (-1 to quit): "))
    if host_idx < 0:
        print("bye")
        return
    public_ip = instance_list[host_idx][4] # 4 is the index of PublicIpAddress
    instance_name = instance_list[host_idx][2] # 2 is the index of Name
    pem = ''
    if args.pem == None:
        home = expanduser("~")
        files = os.listdir(home + "/.aws")
        for f in files:
            if 'pem' in f and instance_name in f:
                pem = home + "/.aws/" + f
                break
        if not pem:
            pem = home + "/.aws/default.pem"
    ssh_cmd = "ssh -i " + pem + " ec2-user@" + public_ip
    print("ssh command: " + ssh_cmd)
    os.system(ssh_cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='designate a pem file')
    parser.add_argument('--pem', '-p', help='a pem file to ssh to aws ec2 instance')
    args = parser.parse_args()
    main(args)

