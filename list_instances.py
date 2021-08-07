#!/usr/bin/env python3

from Ec2 import Ec2

ec2 = Ec2()
instance_list = ec2.get_instance_list(
    ["pending", "running", "stopping", "stopped", "shutting-down", "terminated"])
ec2.print_instance_list(instance_list)