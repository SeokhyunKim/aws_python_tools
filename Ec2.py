import boto3
import tabulate_fns

class Ec2:
    def __init__(self):
        self.ec2 = boto3.client('ec2')

    def get_launch_template_list(self):
        launch_templates = self.ec2.describe_launch_templates()
        #print(launch_templates)
        return tabulate_fns.make_array_for_tabulating(
            keys=["LaunchTemplateId", "LaunchTemplateName", "DefaultVersionNumber", "Tags"],
            json_object_array=launch_templates["LaunchTemplates"])

    def print_launch_template_list(self, launch_template_list = None):
        if launch_template_list == None:
            launch_template_list = self.get_launch_template_list()
        tabulate_fns.print_tabulating_array(
            launch_template_list,
            headers=["Id", "LaunchTemplateId", "LaunchTemplateName", "DefaultVersion", "Tags"])

    def get_instance_list(self, state_filters=["running"]):
        instances_json = self.ec2.describe_instances()
        hosts = []
        id = 0
        for reservation in instances_json["Reservations"]:
            for instance in reservation["Instances"]:
                state = instance["State"]["Name"]
                if state in state_filters:
                    publicIpAddress = ''
                    privateIpAddress = ''
                    if 'PublicIpAddress' in instance:
                        publicIpAddress = instance["PublicIpAddress"]
                    if 'PrivateIpAddress' in instance:
                        privateIpAddress = instance["PrivateIpAddress"]
                    hosts.append([id, instance["InstanceId"], instance["KeyName"], instance["State"]["Name"],
                                  publicIpAddress, privateIpAddress])

                    id += 1
        return hosts

    def print_instance_list(self, instance_list = None):
        if instance_list == None:
            instance_list = self.get_instance_list()
        tabulate_fns.print_tabulating_array(
            instance_list,
            ["Id", "InstanceId", "Name", "State", "PublicIp", "PrivateIp"])

    def start_instances(self, instance_ids):
        self.ec2.start_instances(InstanceIds = instance_ids)

    def stop_instances(self, instance_ids):
        self.ec2.stop_instances(InstanceIds = instance_ids)
