#!/usr/bin/env python3

import os
import shared_fns

def main():
    jsonInstances = shared_fns.describeInstances()
    hosts = shared_fns.getHosts(jsonInstances,
                ["pending", "running", "stopping", "stopped", "shutting-down", "terminated"])

    shared_fns.printTable(hosts,
            ["Id", "InstanceId", "State", "PublicIp", "PrivateIp"])
    hostIds = shared_fns.getHostIdsInput("Type host id to terminate (-1 to quit):")
    if not hostIds:
        print("bye")
        return
    instanceIds = ""
    for hostId in hostIds:
        instanceIds += hosts[hostId][1] + " "
    sshCmd = "aws ec2 terminate-instances --instance-ids " + instanceIds
    print("ssh command: " + sshCmd)
    os.system(sshCmd)

if __name__ == "__main__":
    main()

