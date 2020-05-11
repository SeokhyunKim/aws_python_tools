#!/usr/bin/env python

import ssh_instance

jsonInstances = ssh_instance.ec2DescribeInstancesAsJson()
hosts = ssh_instance.getHosts(jsonInstances)
ssh_instance.printHosts(hosts)
