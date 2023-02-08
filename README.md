# Deploying an AWS t3.medium Instance with Terraform and Ansible

This repository contains Terraform scripts to launch an AWS EC2 t3.medium instance in the default VPC, using an existing key-pair.

## Requirements
- Terraform
- Ansible
- An AWS account
- An existing VPC and key pair in the selected AWS region

## Terraform Configuration
1. Clone the repository
2. Navigate to the `terraform` directory.
3. Set up AWS credentials
Terraform needs to know your AWS access and secret keys to interact with AWS resources. You can set this up by either exporting the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables or by creating a credentials file in the `~/.aws/credentials` directory.
4. Initialize Terraform with the following command:
`terraform init`
5. Plan the Terraform changes with the following command:
`terraform plan -var 'aws_region=<region>' -var 'key_pair_name=<key_pair>'`\
Replace <region> with the AWS region where you want to launch the instance, and <key_pair> with the name of the existing key pair in the selected region.
6. Apply the Terraform changes with the following command:
    `terraform apply -var 'region=us-west-1' -var 'key_pair_name=my-key-pair'`\
    
    Replace `us-west-1` and `my-key-pair` with the desired values for the AWS region and key-pair name.\
    Note the public IP address of the instance from the output of the Terraform apply command. You will need this in the next section.

6. Verify the EC2 instance
Log in to the AWS management console and verify that the EC2 instance has been created.

## Ansible Configuration
1. Navigate to the ansible directory.
2. Install the Docker Compose components on the instance with the following command: `ansible-playbook install-docker-compose.yml -i <public_ip_address>, --private-key <path_to_private_key> -u <remote_user>`\
Replace <public_ip_address> with the public IP address of the instance noted in the Terraform section, <path_to_private_key> with the path to the private key file for the existing key pair, and <remote_user> with the SSH user name for the instance.


## Clean up
To delete the EC2 instance and all associated resources, run the following Terraform command:
`terraform destroy`

## Note
The Terraform scripts assume that there is already a default VPC and an existing key-pair in the specified AWS region. If you need to create these resources, you'll need to modify the Terraform scripts accordingly.







