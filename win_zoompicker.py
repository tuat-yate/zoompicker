import sys
import tkinter as tk
import tkinter.ttk as ttk
import subprocess as sub
import csv
import os
import validators

def init():
    subdict=dict()
    sublist=list()
    classdict=dict()
    print(os.path.dirname(__file__))
    #with open(os.path.dirname(__file__)+'\subname_and_link.csv') as f:
    with open('subname_and_link.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if(len(row)==1):
                row.append('')
                row.append('')
            sublist.append(row[0])
            subdict[row[0]]=row[1]
            classdict[row[0]]=row[2]

    return subdict,sublist,classdict

def call_class(sub_link):
    #print(sub_link)
    if(sub_link!='' and validators.url(sub_link)):
        print(sub_link)
        sub.Popen(['start','chrome',sub_link],shell=True)


def main():

    subdict,sublist,classdict = init()

    # GUI部分の作成
    root = tk.Tk()
    root.title('zoompicker')
    root.geometry('200x150')
    img = tk.Image('photo', file='videoicon.png')
    root.tk.call('wm','iconphoto',root._w,img)
    #root.iconbitmap('videoicon.ico')

    txt=tk.Label(text='')
    txt.pack()

    combo = ttk.Combobox(root, state='readonly')
    combo["values"] = (sublist)
    combo.current(0)
    combo.pack()

    zoom_button = tk.Button(text="zoom起動",command=lambda:call_class(subdict[combo.get()]))
    zoom_button.pack()

    class_button = tk.Button(text="Classroom",command=lambda:call_class(classdict[combo.get()]))
    class_button.pack()

    root.mainloop()

if(__name__=='__main__'):
    main()
