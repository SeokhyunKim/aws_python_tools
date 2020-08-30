aws_python_tools
===========

## easy-to-use aws resource managing cli tool
* [aws cli](https://aws.amazon.com/cli/?nc1=h_ls) is the official cli from AWS.
* But for frequently repeated simple works like start/stop/terminate instances, this tool provides super simple cli interface.
* Currently, can easily check the list of instances, start/stop/terminate instances, create a new instance from launch-template, and ssh to a running instance.

## Prerequisites
* python 3
  * each python script is using '#!/usr/bin/env python3' at the top of py files.
  * may need to change this to '#!/usr/bin/env python' according to your python settings.
* instal [aws python sdk](https://aws.amazon.com/sdk-for-python/)
* install [aws cli](https://aws.amazon.com/cli/?nc1=h_ls)
* install tabulate python module. (if you're using pip for python3, just use pip instead of pip3)
```
pip3 install tabulate
```

## AWS setup
* Need to have access key and secret key for an aws IAM account which have rights to manage ec2 instances.
* To understand IAM account, access key and secret key, check [Understanding and getting your AWS credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html)
* After getting access key and secret key, use 'aws configure' for easy aws credential setup. just run 'aws configure' and provide keys. Then, it is saved as read-only files in ~/.aws/credentials

## How to install
* python scripts. so you can just use *.py files.
* but if you want to make symbolic links under any directory, use make_symlinks
```
./make_symlinks
Target directory: #your preferred target directory
#symlinks for *.py are created under the target directory
```

## What you can do
### list_instances.py
* list instances and some status. e.g.,
```
  Id  InstanceId           State       PublicIp    PrivateIp
----  -------------------  ----------  ----------  -----------
   0  i-000e9d26aab359ad5  terminated
   1  i-0355987ec3577b47e  terminated

```

### create_instance_with_launch_template.py
* create a new instance using a launch-template.
* shows the list of launch-templates.
* can create an instance with launch-template and default version number. e.g.,
```
  Id  LaunchTemplateId      LaunchTemplateName      DefaultVersion
----  --------------------  --------------------  ----------------
   0  lt-03cb3d7d7ac49eb2a  free-tier-version-1                  2
Type launch-template id to create an instance (-1 to quit): 0
```

### ssh_instance.py
* can ssh to a running host very easily. e.g.,
```
  Id  InstanceId           State    PublicIp        PrivateIp
----  -------------------  -------  --------------  ------------
   0  i-0b38f687248cc41d5  running  xx.xx.xx.xx     xx.xx.xx.xx
Type host id to ssh (-1 to quit): 0
ssh command: ssh -i /Users/YOUR_ID/.aws/default_pem ec2-user@xx.xx.xx.xx
Warning: Permanently added 'xx.xx.xx.xx' (ECDSA) to the list of known hosts.

       __|  __|_  )
       _|  (     /   Amazon Linux AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-ami/2018.03-release-notes/
6 package(s) needed for security, out of 10 available
Run "sudo yum update" to apply all updates.
-bash: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
[ec2-user@ip-xx.xx.xx.xx ~]$ 
```
* pem file for ssh
  * can manually give a pem file with '--pem' or '-p' option
  * if a pem file is not specified, ssh_instance.py will try to read it at ~/.aws/default.pem

### start_instances.py
* start multiple instances. e.g.,
```
  Id  InstanceId           State    PublicIp    PrivateIp
----  -------------------  -------  ----------  -------------
   0  i-04ba0a8f9474e4ff0  stopped              xx.xx.xx.xx
Type host ids to start
(separated by space. -1 to quit): 0
```

### stop_instances.py
* stop multiple instances. e.g.,
```
  Id  InstanceId           State    PublicIp       PrivateIp
----  -------------------  -------  -------------  -------------
   0  i-04ba0a8f9474e4ff0  running  xx.xx.xx.xx    xx.xx.xx.xx
Type host ids to stop
(separated by space. -1 to quit): 0
```

### terminate_instances.py
* terminate multiple instances. e.g.,
```
  Id  InstanceId           State       PublicIp     PrivateIp
----  -------------------  ----------  -----------  -------------
   0  i-000e9d26aab359ad5  terminated
   1  i-0355987ec3577b47e  running     xx.xx.xx.xx.  xx.xx.xx.xx
   2  i-04ba0a8f9474e4ff0  running     xx.xx.xx.xx.  xx.xx.xx.xx
Type host ids to terminate
(separated by space. -1 to quit): 1 2
```
