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
    
completed_tasks_question = input("Did you complete any tasks? Enter 'y' for yes. All other answers are no.")
if completed_tasks_question.lower() == 'y':
    while True:
        task_completed = int(input("Enter the task number of the task you have completed: "))
        for key, value in todolist.items():
            if key == task_completed:
                todolist[task_completed] = f"{value} (complete)"
        more_completed_tasks = input("Did you finish any other tasks? Enter any key for yes.")
        if not more_completed_tasks:
            print("This is your list now:")
            print(todolist)
            break

print(" ")
delete_tasks = input("Would you like to delete tasks? Input 'y' for yes. Any other key is no.")
if delete_tasks == 'y':
    tasks_to_delete = input("Enter the task numbers you want to delete, each number separated by a space: ")
    list_of_tasks_to_delete = list(tasks_to_delete.split())
    todolist_keys = list(todolist.keys())
    for key in todolist_keys:
        if str(key) in list_of_tasks_to_delete:
            del todolist[key]
else:
     print("No tasks will be deleted")
   

print(" ")
print("Your new to do list is:")
print(todolist)
