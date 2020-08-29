#!/usr/bin/env python3

import os
import ssh_instance

def main():
    jsonInstances = ssh_instance.ec2DescribeInstancesAsJson()
    hosts = ssh_instance.getHosts(jsonInstances)
    ssh_instance.printHosts(hosts)
    hostIdx = int(input("Type host id to terminate (-1 to quit): "))
    if hostIdx < 0:
        print("bye")
        return
    instanceId = hosts[hostIdx][1] 
    sshCmd = "aws ec2 terminate-instances --instance-ids " + instanceId
    print("ssh command: " + sshCmd)
    os.system(sshCmd)

if __name__ == "__main__":
    main()

