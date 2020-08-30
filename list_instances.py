#!/usr/bin/env python3

import shared_fns

jsonInstances = shared_fns.describeInstances()
hosts = shared_fns.getHosts(jsonInstances,
            ["pending", "running", "stopping", "stopped", "shutting-down", "terminated"])
shared_fns.printTable(hosts,
        ["Id", "InstanceId", "State", "PublicIp", "PrivateIp"])

