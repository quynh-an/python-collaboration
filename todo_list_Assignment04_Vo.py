#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:16:56 2024

@author: tandyllc
"""

print("You are about to create a to-do list.")

while True:
    tasks = input("Press any key to add a task. ")
    if tasks:
        todolist = dict({})
    for i in range(0,101):    
        todolist[i+1] = input("Enter your task. Type 'n' if you no longer want to add tasks. ")
        if todolist[i+1] == 'n':
            del todolist[i+1]
            break
    break

view_todo = input("Enter any key to view your to do list. No key means no list will be shown. ")
if view_todo:
    print("Here are all your tasks: ")
    print(" ")
    print(todolist)
else: 
    print("You did not request to show your list.")