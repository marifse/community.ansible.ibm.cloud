
ibm.container_storage_attachment_delete module -- Remove volume storage from worker node in kubernetes cluster 
==============================================================================================================

Note

This module is part of the ibm collection (version 1.0.0).

To install it, use: ansible-galaxy collection install ibm. You need further requirements to be able to use this module, see :ref:`Requirements <ansible_collections.ibm.ibm_container_storage_attachment_delete_module_requirements>` for details.

To use it in a playbook, specify: :code:`ibm.container_storage_attachment_delete`.

.. contents::
   :local:
   :depth: 1

.. Deprecated

Synopsis
--------

This module removes the attached block storage volume from worker node in an IBM Kubernetes cluster.

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
      <p class="ansible-option-line"><span class="ansible-option-choices">Cluster Name / ID, on which the image security is to be disabled:</span></p>
    </div></td>
  </tr>
 <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-volumeAttachmentID"></div>
      <p class="ansible-option-title"><strong>volumeAttachmentID</strong></p>
      <a class="ansibleOptionLink" href="#parameter-volumeAttachmentID" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Volume Attachment ID.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">The volume attachment id, can be fetched using IBM Cloud CLI</span></p>
    </div></td>
  </tr>
 <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-worker"></div>
      <p class="ansible-option-title"><strong>worker</strong></p>
      <a class="ansibleOptionLink" href="#parameter-worker" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Worker Node ID.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">The worker node on which the volume is required to be attached:</span></p>
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

   - name: Detach volume storage from worker node in an IBM Kubernetes Cluster
     hosts: localhost
     tasks:
       ibm.container_storage_attachment_delete:
         ibmcloud_api_key: "{{ ibmcloud_api_key }}"
         resource_group_id: "{{ resource_group_id }}"
         config:
           cluster: "Your Cluster ID"
           volumeAttachmentID: "Volume Attachment ID"
           worker: "Worker Node ID"
      

Authors
~~~~~~~

- Muhammad Arif (@marifse)
