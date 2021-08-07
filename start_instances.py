#!/usr/bin/env python3

from shared_functions import *
from Ec2 import Ec2

def main():
    ec2 = Ec2()
    hosts = ec2.get_instance_list(["stopped"])
    ec2.print_instance_list(hosts)
    hostIds = get_host_ids_from_input("Type host ids to start\n(separated by space. -1 to quit):")
    if not hostIds:
        print("bye")
        return
    instanceIds = []
    for hostId in hostIds:
        instanceIds.append(hosts[hostId][1])
    ec2.start_instances(instanceIds)

if __name__ == "__main__":
    main()
