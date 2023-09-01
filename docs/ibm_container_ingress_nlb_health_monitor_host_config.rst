ibm.container_ingress_nlb_health_monitor_host_config module -- View the health check monitor settings for an NLB subdomain.
===========================================================================================================================

Note

This module is part of the ibm collection (version 1.0.0).

To install it, use: ansible-galaxy collection install ibm. You need further requirements to be able to use this module, see :ref:`Requirements <ansible_collections.ibm.ibm_container_ingress_nlb_health_monitor_host_config_module_requirements>` for details.

To use it in a playbook, specify: :code:`ibm.container_ingress_nlb_health_monitor_host_config`.

.. contents::
   :local:
   :depth: 1

.. Deprecated

Synopsis
--------

- This module view the health check monitor settings for an NLB subdomain.

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
      <div class="ansibleOptionAnchor" id="parameter-idOrName"></div>
      <p class="ansible-option-title"><strong>idOrName</strong></p>
      <a class="ansibleOptionLink" href="#parameter-idOrName" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Cluster Name.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Cluster Name / ID, on which to enable a health check monitor for an existing NLB subdomain:</span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-nlbHost:"></div>
      <p class="ansible-option-title"><strong>nlbHost:</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nlbHost:" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>NLB Host Domain Name</p>
      <p class="ansible-option-line"><span class="ansible-option-choices"></span></p>
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

   - name: Create and optionally enable a health check monitor for an existing NLB subdomain in a cluster
     hosts: localhost
     tasks:
       ibm.container_ingress_nlb_health_monitor_config:
         ibmcloud_api_key: "{{ ibmcloud_api_key }}"
         resource_group_id: "{{ resource_group_id }}"
         config:
           idOrName: "Cluster Name / ID, on which to list the settings for all existing health check monitors"
           nlbHost: "NLB Host Domain Name"
      

Authors
~~~~~~~

- Muhammad Arif (@marifse)
