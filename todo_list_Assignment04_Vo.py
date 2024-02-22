#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:16:56 2024

@author: tandyllc
"""

def move_tasks(todo_dict):
    write_file = 'todo_today.txt'
    while True:
        task_to_move = input("Enter a task number to move to another file. Press a character to stop. " )
        if not task_to_move.isdigit():
            break
        task_to_move = int(task_to_move)
        if task_to_move in todo_dict:
            with open(write_file, 'a') as file:
                file.write(f"{task_to_move}: {todo_dict[task_to_move]}\n")
        else:
            print("Task not found in the list.")
    return write_file

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

print(" ")
view_todo = input("Enter any key to view your to do list. No key means no list will be shown. ")
if view_todo:
    print(" ")
    print("Here are all your tasks: ")
    print(" ")
    print(todolist)
else: 
    print("You did not request to show your list.")
    
print(" ")
completed_tasks_question = input("Did you complete any tasks? Enter 'y' for yes. All other answers are no. ")
if completed_tasks_question.lower() == 'y':
    copy_todolist = todolist
    while True:
        task_completed = input("Enter the task number of the task you have completed. For no more tasks, enter 'n'. ")
        for key, value in copy_todolist.items():
            if task_completed.lower() == 'n':
                break
            if key == int(task_completed): 
                todolist[key] = f"{value} (complete)"
        more_completed_tasks = input("Did you finish any other tasks? Enter any key for yes. Press enter to move on. ")
        if not more_completed_tasks:
            print(" ")
            print("This is your list now: ")
            print(todolist)
            break

print(" ")
delete_tasks = input("Would you like to delete tasks? Input 'y' for yes. Any other key is no. ")
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
print("Your to do list is:")
print(todolist)
print(" ")

ask_to_move_to_file = input("Do you want to move tasks to another file? Enter 'y' for yes. ")
if ask_to_move_to_file.lower() == 'y':
   move_tasks(todolist)
   print("Tasks have been added to a file.")
else:
    print("You did not select to move tasks to another file.")


