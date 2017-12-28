#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:09:15 2017

@author: nguyentran

This is a client for submitting definitions of workflows and tasks to a conductor server
The implementation is based on the python library included in the repository of netflix
"""

from conductor import conductor
from functools import wraps
import json

WF_SERVER_PATH = "http://localhost:8080/api"

def getJSON(pathJSON):
    print(pathJSON)
    read_data = ""
    with open(pathJSON) as f:
        read_data = json.load(f)
    return read_data

def add_workflow(pathJSON):
    wf_def = getJSON(pathJSON)
    metaClient = conductor.MetadataClient(WF_SERVER_PATH)
    print(metaClient.createWorkflowDef(wf_def))
    print("Finish adding workflow at %s" % pathJSON)

def add_task(pathJSON):
    task_def = getJSON(pathJSON)
    metaClient = conductor.MetadataClient(WF_SERVER_PATH)
    print(metaClient.registerTaskDefs(task_def))
    print("Finish adding workflow at %s" % pathJSON)

def start_wf(wfName, inputjson):
    wf_client = conductor.WorkflowClient(WF_SERVER_PATH)
    wf_client.startWorkflow(wfName = wfName, inputjson = inputjson)
    print("Finish invoking workflow %s" % wfName)

# Output of a finished workout is stored in the description of the workflow instance
# This function retrieve representation of a workflow instance
def get_wf(wfId):
    wf_client = conductor.WorkflowClient(WF_SERVER_PATH)
    return wf_client.getWorkflow(wfId, includeTasks=False)
    

if __name__ == "__main__":
#    add_workflow("./sample_defs/wf_def.json")
#    add_task("./sample_defs/task_def.json")
#    start_wf(wfName = "wf_hello", inputjson = {"hello" : "Hello! This is from workflow input."})
    print(get_wf("128876b5-9d90-4eb0-b7f8-bbcf53e8beb5")["output"])