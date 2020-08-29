#!/usr/bin/env python3

import os
import json
import argparse
from tabulate import tabulate
from os.path import expanduser

def ec2DescribeInstancesAsJson():
    stream = os.popen('aws ec2 describe-instances')
    output = stream.read()
    return json.loads(output)

def getHosts(jsonInstances):
    hosts = []
    id = 0
    for reservation in jsonInstances["Reservations"]:
        for instance in reservation["Instances"]:
            if 'PublicIpAddress' in instance:
                hosts.append([id, instance["InstanceId"], instance["State"]["Name"],
                            instance["PublicIpAddress"], instance["PrivateIpAddress"]])
                id += 1
    return hosts

def printHosts(hosts):
    headers = ["Id", "InstanceId", "State", "PublicIp", "PrivateIp"]
    print(tabulate(hosts, headers=headers))

def main(args):
    jsonInstances = ec2DescribeInstancesAsJson()
    hosts = getHosts(jsonInstances)
    printHosts(hosts)
    hostIdx = int(input("Type host id to ssh: "))
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
        defaultPem = open(home + "/.aws/default_pem", "r")
        args.pem = defaultPem.read().rstrip()
    main(args)

