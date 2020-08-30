#!/usr/bin/env python3

import shared_fns

def main():
    client = shared_fns.createEc2Client()
    jsonInstances = shared_fns.describeInstances(client)
    hosts = shared_fns.getHosts(jsonInstances)
    shared_fns.printTable(hosts,
              ["Id", "InstanceId", "State", "PublicIp", "PrivateIp"])
    hostIds = shared_fns.getHostIdsInput("Type host id to stop (-1 to quit):")
    if not hostIds:
        print("bye")
        return
    instanceIds = []
    for hostId in hostIds:
        instanceIds.append(hosts[hostId][1])
    client.stop_instances(InstanceIds=instanceIds)

if __name__ == "__main__":
    main()
