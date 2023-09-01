ibm.container_ingress_nlb_health_monitor_config module -- Create and optionally enable a health check monitor for an existing NLB subdomain in a cluster.
========================================================================================================================================================

Note

This module is part of the ibm collection (version 1.0.0).

To install it, use: ansible-galaxy collection install ibm. You need further requirements to be able to use this module, see :ref:`Requirements <ansible_collections.ibm.ibm_container_ingress_nlb_health_monitor_config_module_requirements>` for details.

To use it in a playbook, specify: :code:`ibm.container_ingress_nlb_health_monitor_config`.

.. contents::
   :local:
   :depth: 1

.. Deprecated

Synopsis
--------

- This module create and optionally enable a health check monitor for an existing NLB subdomain in a cluster.

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
      <div class="ansibleOptionAnchor" id="parameter-clusterID"></div>
      <p class="ansible-option-title"><strong>clusterID</strong></p>
      <a class="ansibleOptionLink" href="#parameter-clusterID" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Cluster ID.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Cluster ID, on which to enable a health check monitor for an existing NLB subdomain:</span></p>
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
      <div class="ansibleOptionAnchor" id="parameter-allowInsecureSet"></div>
      <p class="ansible-option-title"><strong>allowInsecureSet</strong></p>
      <a class="ansibleOptionLink" href="#parameter-idOrName" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">Boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>True or False</p>
      <p class="ansible-option-line"><span class="ansible-option-choices"></span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-healthcheckProperties"></div>
      <p class="ansible-option-title"><strong>healthcheckProperties</strong></p>
      <a class="ansibleOptionLink" href="#parameter-idOrName" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>backend-pool</p>
      <p class="ansible-option-line"><span class="ansible-option-choices"></span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-desc"></div>
      <p class="ansible-option-title"><strong>desc</strong></p>
      <a class="ansibleOptionLink" href="#parameter-desc" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Monitor State</p>
      <p class="ansible-option-line"><span class="ansible-option-choices"></span></p>
    </div></td>
  </tr>
   <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-followRedirectSet"></div>
      <p class="ansible-option-title"><strong>followRedirectSet</strong></p>
      <a class="ansibleOptionLink" href="#parameter-followRedirectSet" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>/</p>
      <p class="ansible-option-line"><span class="ansible-option-choices"></span></p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-healtcheckPropertiesSetStatus"></div>
      <p class="ansible-option-title"><strong>healtcheckPropertiesSetStatus</strong></p>
      <a class="ansibleOptionLink" href="#parameter-healtcheckPropertiesSetStatus" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>enabled or disabled</p>
      <p class="ansible-option-line"><span class="ansible-option-choices"></span></p>
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
           clusterID: "Your Cluster ID"
           idOrName: "Cluster Name / ID, on which to list the settings for all existing health check monitors"
           allowInsecureSet: "true"
           healthcheckProperties: "backend-pool"
           desc: "Monitor State"
           followRedirectSet: "/"
           healtcheckPropertiesSetStatus: "enabled || disabled"
           nlbHost: "NLB Host Domain Name"
      

Authors
~~~~~~~

- Muhammad Arif (@marifse)
