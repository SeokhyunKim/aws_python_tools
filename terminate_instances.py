#!/usr/bin/env python3

import os
from Ec2 import Ec2
from shared_functions import *

def main():
    ec2 = Ec2()
    instance_list = ec2.get_instance_list(
        ["pending", "running", "stopping", "stopped", "shutting-down", "terminated"])
    ec2.print_instance_list(instance_list)
    hostIds = get_host_ids_from_input("Type host ids to terminate\n(separated by space. -1 to quit):")
    if not hostIds:
        print("bye")
        return
    instanceIds = ""
    for hostId in hostIds:
        instanceIds += instance_list[hostId][1] + " "
    sshCmd = "aws ec2 terminate-instances --instance-ids " + instanceIds
    #print("ssh command: " + sshCmd)
    print("To terminate these instances, open terminate_instance.py and activate start_instance command: " + instanceIds)
    #os.system(sshCmd)

if __name__ == "__main__":
    main()

