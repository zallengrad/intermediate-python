import tkinter as tk

def add(*args) :
    sum = 0
    for i in args:
        sum += i
    return (sum)

add(5,4,5)