#!/usr/bin/env python3

import boto3
import os
import time

environment = 'tooling'
region = 'us-east-1'
worker_group = 'worker'
#instances = []

client = boto3.client('ec2',region_name=region)

response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                "cxd-eks-{}-{}-{}".format(environment,region,worker_group),
            ]
        },
        {   'Name': 'instance-state-name',
            'Values': [
                "running",
            ] 
        },
    ],
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        node = instance['PrivateDnsName']
        print("****** Draining Node: {} ******".format(node))
        os.system('kubectl cordon ' + node)
        os.system('kubectl drain {} --ignore-daemonsets --delete-local-data'.format(node))
        print("****** CORDON COMPLETE! ******")
        time.sleep(5)
        print("Terminating the Node ...")
        client.terminate_instances(InstanceIds=[instance['InstanceId']])
        time.sleep(125)
        #instances.append(instance['InstanceId'])
        
# print(instances)
# time.sleep(300)
# if instances:
#     terminate_resp = client.terminate_instances(InstanceIds=instances)
#     print(terminate_resp)

