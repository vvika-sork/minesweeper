from tkinter import*
from random import randint

mine = True
row = True
column = True

def click_diff_e(mine, row, column):
    mine = 10 
    row = 9
    column = 9
    top.destroy()
    return mine, row, column

def click_diff_m(mine, row, column):
    mine = 40 
    row = 16
    column = 16
    top.destroy()
    return mine, row, column

def click_diff_h(mine, row, column):
    mine = 90 
    row = 16
    column = 30
    top.destroy()
    return mine, row, column
 
def player_win():
    for y in range(len(w)):
        for x in range(len(w[0])):
            if m[y][x]==0 and w[y][x]["text"]=="F":
                return False
            if w[y][x]["text"]==" ":
                return False
    return True
 
def restart_game():
    global m,w, label,mine, row, column 
    m = make_matrix(mine, row, column)
    for y in range(len(w)):
        for x in range(len(w[0])):
            w[y][x]["text"]=" "
            w[y][x]["state"]="normal"
    label.pack_forget()
 
def create_right_button_click(b):
    def right_button_click(e):
        global label
        if player_win():
            label = Label(t, text="Ви виграли!", bg='green')
            label.pack()
        if b["text"]==" ":
            b["text"]="F"
        elif b["text"]=="F":
            b["text"]=" "
    return right_button_click
 
def make_matrix(z,width,height):
    global m,w, mine
    mi = mine
    h=[]
    for i in range(height):
        d=[]
        for j in range(width):
            d=d+[0]
        h=h+[d]
    while mi != 0:
        y=randint(0,len(h)-1)
        x=randint(0,len(h[0])-1)
        h[y][x] = 1
        mi -= 1            
    return h
 
def open_cell(y,x):
    if y>=len(w) or y<0 or x>=len(w[0]) or x<0:
        return
    else:
        if w[y][x]['text']==' ':
            w[y][x]['text']=count(y,x)
            w[y][x]["state"]="disabled"
            if count(y,x)==0:
                open_cell(y,x+1)
                open_cell(y,x-1)
                open_cell(y+1,x)
                open_cell(y-1,x)
                open_cell(y+1,x+1)
                open_cell(y-1,x-1)
                open_cell(y-1,x+1)
                open_cell(y+1,x-1)
 
def get(y,x):
    if y>=len(m) or x>=len(m[0]) or y<0 or x<0:
        return 0
    else:
        return m[y][x]
 
def count(y,x):
    return get(y,x+1)+\
           get(y,x-1)+\
           get(y+1,x)+\
           get(y-1,x)+\
           get(y+1,x+1)+\
           get(y-1,x-1)+\
           get(y-1,x+1)+\
           get(y+1,x-1)
           
 
def create_sapor(y,x,b):
    def sapor():
        global label
        if player_win():
            label = Label(t, text="Ви виграли!", bg='green')
            label.pack()
        else:
            if m[y][x]==1:
                b['text']='*'
                label = Label(t, text="Ви програли!!", bg='red')
                label.pack()
                for y1 in range(len(m)):
                    for x1 in range(len(m[0])):
                            w[y1][x1]["state"]="disabled"
                            if m[y1][x1]==1:
                                w[y1][x1]["text"]="*"
            else:
                open_cell(y,x)
    return sapor

t = Tk()
top = Toplevel()
top.geometry("100x100")

Label(top, text="Оберіть складність:").pack()
   
btn1 = Button(top, text="EASY", command=lambda:click_diff_e(mine, row, column))
btn1.pack()

btn2 = Button(top, text="MEDIUM", command=lambda:click_diff_m(mine, row, column))
btn2.pack()

btn3 = Button(top, text="HARD", command=lambda:click_diff_h(mine, row, column))
btn3.pack()

m = make_matrix(mine, row, column)

w=[]
f=Frame(t)
f.pack()
for y in range(len(m)):
    n=[]
    for x in range(len(m[0])):
        b = Button(f,text=' ',width=2)
        b.bind("<Button-3>",create_right_button_click(b))
        b.grid(row=y,column=x)
        b["command"]=create_sapor(y,x,b)
        n=n+[b]
    w=w+[n]
restart_button=Button(t,text='Restart',command=restart_game)
restart_button.pack()
t.withdraw()
t.mainloop()
