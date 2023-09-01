ibm.container_ingress_alb_enable   module -- Enable an existing ALB in a VPC cluster.
====================================================================================

Note

This module is part of the ibm collection (version 1.0.0).

To install it, use: ansible-galaxy collection install ibm. You need further requirements to be able to use this module, see :ref:`Requirements <ansible_collections.ibm.ibm_container_ingress_alb_enable_module_requirements>` for details.

To use it in a playbook, specify: :code:`ibm.container_ingress_alb_enable`.

.. contents::
   :local:
   :depth: 1

.. Deprecated

Synopsis
--------

- This module enables an existing ALB in a VPC cluster.

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
      <p>Cluster Name / ID.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Cluster on which the ingress ALB is desired to be created</span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-albID"></div>
      <p class="ansible-option-title"><strong>albID</strong></p>
      <a class="ansibleOptionLink" href="#parameter-albID" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>ALB ID.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">The load balancer id</span></p>
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

   - name: Enable a public or private ALB in a specified zone and VPC cluster
     hosts: localhost
     tasks:
       ibm.container_ingress_alb_enable:
         ibmcloud_api_key: "{{ ibmcloud_api_key }}"
         resource_group_id: "{{ resource_group_id }}"
         config:
           cluster: "Your Cluster Name / ID"
           albID: "The ingress ALB id"
      
      

Authors
~~~~~~~

- Muhammad Arif (@marifse)

