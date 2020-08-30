#!/usr/bin/env python3

import os
import shared_fns
import argparse
from os.path import expanduser

def main(args):
    jsonInstances = shared_fns.describeInstances()
    hosts = shared_fns.getHosts(jsonInstances)
    shared_fns.printTable(hosts,
                ["Id", "InstanceId", "State", "PublicIp", "PrivateIp"])
    hostIdx = int(input("Type host id to ssh (-1 to quit): "))
    if hostIdx < 0:
        print("bye")
        return
    publicIp = hosts[hostIdx][3] # 3 is the index of PublicIpAddress
    sshCmd = "ssh -i " + args.pem + " ec2-user@" + publicIp
    print("ssh command: " + sshCmd)
    os.system(sshCmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='designate a pem file')
    parser.add_argument('--pem', '-p', help='a pem file to ssh to aws ec2 instance')
    args = parser.parse_args()
    if args.pem == None:
        home = expanduser("~")
        args.pem = home + "/.aws/default.pem"
    main(args)

