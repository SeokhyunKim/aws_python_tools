#!/usr/bin/env python3

import os
import shared_fns
    
def main():
    launchTemplatesJson = shared_fns.describeLaunchTemplates()
    launchTemplates = shared_fns.makeArrayForTabulating(keys=["LaunchTemplateId", "LaunchTemplateName", "DefaultVersionNumber"],
                                                        jsonObjectArray = launchTemplatesJson["LaunchTemplates"])
    shared_fns.printTable(launchTemplates, ["Id", "LaunchTemplateId", "LaunchTemplateName", "DefaultVersion"])
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
