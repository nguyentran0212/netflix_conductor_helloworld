#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:43:44 2017

@author: nguyentran

This module shows the client of a worker service. This client is a part of the worker service.
It is responsible for interacting with a conductor server.
When receive a new task, it invokes a corresponding function on the service
When the function finishes, it updates the task status to the conductor server
"""

from conductor.ConductorWorker import ConductorWorker

# This function is called when the task handled by this service is detected on the conductor server
def execute(task):
    print(task)
#    return None
    return {'status': 'COMPLETED', 'output': {"helloOutput" : task['inputData']['helloInput'] + " And this is appended from hello task"}, 'logs' : []}

def exc(taskType, inputData, startTime, retryCount, status, callbackAfterSeconds, pollCount):
    print('Executing the function')
    return {'status': 'COMPLETED', 'output': {'helloOutput' : 'output from the hello task'}}

def main():
    print('Hello World')
    # Create a conductor worker client
    # Args: location of WF server, number of threads, and polling interval
    cc = ConductorWorker('http://localhost:8080/api', 1, 0.1)
	# Start polling for task
    cc.start('hello_task', execute, True)
    
if __name__ == '__main__':
    main()