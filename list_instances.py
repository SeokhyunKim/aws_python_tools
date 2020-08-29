#!/usr/bin/env python3

import ssh_instance

jsonInstances = ssh_instance.ec2DescribeInstancesAsJson()
hosts = ssh_instance.getHosts(jsonInstances)
ssh_instance.printHosts(hosts)
