#!/usr/bin/env python3

import os
from Ec2 import Ec2

def main():
    ec2 = Ec2()
    launch_template_list = ec2.get_launch_template_list()
    ec2.print_launch_template_list(launch_template_list)
    template_idx = int(input("Type launch-template id to create an instance (-1 to quit): "))
    if template_idx < 0:
        print("bye")
        return
    launch_template_id = launch_template_list[template_idx][1]
    # Looks like boto3 does not provide instance creation with template-id
    sshCmd = "aws ec2 run-instances --launch-template LaunchTemplateId=" + launch_template_id
    # print("command: " + sshCmd)
    os.system(sshCmd)

if __name__ == "__main__":
    main()