ibm.container_monitoring_config_modify module -- Modify config monitoring instance to an IBM Kubernetes Cluster
======================================================================================================================

Note

This module is part of the ibm collection (version 1.0.0).

To install it, use: ansible-galaxy collection install ibm. You need further requirements to be able to use this module, see :ref:`Requirements <ansible_collections.ibm.ibm_container_monitoring_config_modify_module_requirements>` for details.

To use it in a playbook, specify: :code:`ibm.container_monitoring_config_modify`.

.. contents::
   :local:
   :depth: 1

.. Deprecated

Synopsis
--------

- This module change / replace the existing monitoring instance attached to an IBM Kubernetes Cluster to a new one.

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
      <p class="ansible-option-line"><span class="ansible-option-choices">Cluster Name / ID, on which the image security is to be enabled:</span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-instance"></div>
      <p class="ansible-option-title"><strong>instance</strong></p>
      <a class="ansibleOptionLink" href="#parameter-instance" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Existing Monitoring Instance ID</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">The existing monitoring config instance Id attached to IBM Kubernetes Cluster</span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-newInstance"></div>
      <p class="ansible-option-title"><strong>newInstance</strong></p>
      <a class="ansibleOptionLink" href="#parameter-instance" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>New Monitoring Instance ID</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">The new monitoring config instance Id to be attached to IBM Kubernetes Cluster</span></p>
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

   - name: Modify the existing monitoring instance to new monitoring instance in IBM Kubernetes Cluster
     hosts: localhost
     tasks:
       ibm.container_monitoring_config_modify:
         ibmcloud_api_key: "{{ ibmcloud_api_key }}"
         config:
           cluster: "Your Cluster Name / ID"
           instance: "Existing Monitoring Instance ID"
           newInstance: "New Monitoring Instance ID"

Authors
~~~~~~~

- Muhammad Arif (@marifse)
