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
    public_ip = instance_list[host_idx][3] # 3 is the index of PublicIpAddress
    ssh_cmd = "ssh -i " + args.pem + " ec2-user@" + public_ip
    #print("ssh command: " + ssh_cmd)
    os.system(ssh_cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='designate a pem file')
    parser.add_argument('--pem', '-p', help='a pem file to ssh to aws ec2 instance')
    args = parser.parse_args()
    if args.pem == None:
        home = expanduser("~")
        args.pem = home + "/.aws/default.pem"
    main(args)

