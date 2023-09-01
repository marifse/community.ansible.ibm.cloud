ibm.container_ingress_nlb_delete_secret module -- Delete Ingres NLB secret in an IBM Kubernetes Cluster
=======================================================================================================

Note

This module is part of the ibm collection (version 1.0.0).

To install it, use: ansible-galaxy collection install ibm. You need further requirements to be able to use this module, see :ref:`Requirements <ansible_collections.ibm.ibm_container_ingress_nlb_delete_secret_module_requirements>` for details.

To use it in a playbook, specify: :code:`ibm.container_ingress_nlb_delete_secret`.

.. contents::
   :local:
   :depth: 1

.. Deprecated

Synopsis
--------

This module deletes the Ingress NLB secret in an IBM Kubernetes cluster.

Requirements
------------

The below requirements are needed on the host that executes this module.

- Ansible


Parameters
----------


.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Parameter</p></th>
    <th class="head"><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-ibmcloud_api_key"></div>
      <p class="ansible-option-title"><strong>ibmcloud_api_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ibmcloud_api_key" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The IBM Cloud API Key. Can be provided in the ./inventory/main.cfg</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-resource_group_id"></div>
      <p class="ansible-option-title"><strong>resource_group_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_group_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The ResourceGroup ID</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-cluster"></div>
      <p class="ansible-option-title"><strong>cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Cluster Name.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Cluster Name / ID, on which the ingress nlb secret is to be deleted for:</span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-subDomain"></div>
      <p class="ansible-option-title"><strong>subDomain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-subDomain" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Sub-domain</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">The ingress subdomain of kubernetes cluster on which the secret is desired to be deleted</span></p>
    </div></td>
  </tr>
  </tbody>
  </table>



.. Attributes


.. Notes


.. Seealso


.. Examples


Examples
--------

Example usage:

.. code-block:: yaml

   - name: Deletes an ingress nlb secret in an IBM Kubernetes Cluster
     hosts: localhost
     tasks:
       ibm.container_ingress_nlb_delete_secret:
         ibmcloud_api_key: "{{ ibmcloud_api_key }}"
         resource_group_id: "{{ resource_group_id }}"
         config:
           cluster: "Your Cluster ID"
           subDomain: "The subdomain of the ingress NLB in kubernetes cluster"

Authors
~~~~~~~

- Muhammad Arif (@marifse)
