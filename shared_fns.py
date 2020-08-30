import boto3
from tabulate import tabulate

def createEc2Client():
    return boto3.client('ec2')

def describeLaunchTemplates(client=None):
    if client == None: 
        client = createEc2Client()
    return client.describe_launch_templates()

def describeInstances(client=None):
    if client == None: 
        client = createEc2Client()
    client = createEc2Client()
    return client.describe_instances()

def makeArrayForTabulating(keys, jsonObjectArray):
    tabulateAry = []
    id = 0;
    for jsonObj in jsonObjectArray:
        tabulateItem = []
        tabulateItem.append(id)
        id += 1
        for key in keys:
            tabulateItem.append(jsonObj[key])
        tabulateAry.append(tabulateItem)
    return tabulateAry

def getHosts(jsonInstances, stateFilters=["running"]):
    hosts = []
    id = 0
    for reservation in jsonInstances["Reservations"]:
        for instance in reservation["Instances"]:
            state = instance["State"]["Name"]
            if state in stateFilters:
                publicIpAddress = ''
                privateIpAddress = ''
                if 'PublicIpAddress' in instance:
                    publicIpAddress = instance["PublicIpAddress"]
                if 'PrivateIpAddress' in instance:
                    privateIpAddress = instance["PrivateIpAddress"]
                hosts.append([id, instance["InstanceId"], instance["State"]["Name"],
                             publicIpAddress, privateIpAddress])
                id += 1
    return hosts

def printTable(tabulatingArray, headers):
    print(tabulate(tabulatingArray, headers=headers))

def getHostIdsInput(guideText):
    inputString = input(guideText + " ")
    hostIdStrings = inputString.split(" ")
    hostIds = []
    for hostIdStr in hostIdStrings:
        hostId = int(hostIdStr)
        if hostId < 0:
            return []
        hostIds.append(hostId)
    return hostIds

