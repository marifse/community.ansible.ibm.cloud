# IBM Cloud Kubernetes Ansible Collections

Ansible modules collection for IBM cloud.

## Getting Started
Below steps are follwed to install ansible collections for the IBM Cloud resources. All the resources are documented under the [Docs] directory.

## Prerequisites

1. [Install ansible].

2.  To install ansible on Ubuntu 20.04, run the below command: 

    ```
    sudo apt install ansible -y
    ```


    **Note**: These automation playbooks have been tested on ansible 2.9.6 on ubuntu 20.04.

## Install & Build the Collection

1. Build and Install collection
    
    ```
    ansible-galaxy collection build
    ```

    ```
    ansible-galaxy collection install collection_name.tar
    ```
2.  Set the path in ansible.cfg and the api key in inventory/main.cfg

## Running the Playbooks

1. Go into your cloned repo main directory with below command.
    
    ```
    cd community_ibm_iks_ansible_collection
    ```

2. Modify any playbook yaml file to set the variables, like to enable image security, modify the file and change the IKS cluster id in that

    ```
    vi ibm/custom_iks_collection/examples/manage_image_security/image_security_enable.yaml
    ```
   
2. Run the playbook

    ```
    ansible-playbook ibm/custom_iks_collection/examples/manage_image_security/image_security_enable.yaml
    ```
    
### Example Projects

1. [Manage Storage Attachment](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_storage_attachment)

2. [Manage Config Monitoring](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_config_monitoring)

3. [Manage IKS Cluster](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_iks_cluster)

4. [Manage IKS Image Security](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_image_security)

5. [Manage Ingress ALB for IKS](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_ingress_alb)

6. [Manage NLB Health Monitor](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_nlb_health_monitor)

7. [Manage Private/Public Service Endpoints](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_private_public_service_endpoint)

8. [Manage Secrets for IKS](https://github.com/marifse/community_ibm_iks_ansible_collections/tree/main/ibm/custom_iks_collection/examples/iks_vpc_cluster/manage_secret)


[Install ansible]: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
[Docs]: https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/docs

