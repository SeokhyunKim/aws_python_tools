#!/usr/bin/env python3

import os
import json
from tabulate import tabulate

def ec2DescribeLaunchTemplatesAsJson():
    stream = os.popen('aws ec2 describe-launch-templates')
    output = stream.read()
    return json.loads(output)

def getLaunchTemplates(jsonLaunchTemplates):
    templates = []
    id = 0
    templatesArray = jsonLaunchTemplates["LaunchTemplates"]
    for template in templatesArray:
        templates.append([id, template["LaunchTemplateId"], template["LaunchTemplateName"], template["DefaultVersionNumber"]])
        id += 1
    return templates

def printTemplates(templates):
    headers = ["Id", "LaunchTemplateId", "LaunchTemplateName", "DefaultVersion"]
    print(tabulate(templates, headers=headers))
    
def main():
    launchTemplatesJson = ec2DescribeLaunchTemplatesAsJson()
    launchTemplates = getLaunchTemplates(launchTemplatesJson)
    printTemplates(launchTemplates)
    templateIdx = int(input("Type launch-template id to create an instance (-1 to quit): "))
    if templateIdx < 0:
        print("bye")
        return
    launchTemplateId = launchTemplates[templateIdx][1]
    sshCmd = "aws ec2 run-instances --launch-template LaunchTemplateId=" + launchTemplateId
    print("command: " + sshCmd)
    os.system(sshCmd)
    
if __name__ == "__main__":
    main()