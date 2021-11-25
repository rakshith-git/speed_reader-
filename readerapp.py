from turtle import*
import time
tracer(0)

delay=0.05
f=open(r"C:\Users\Lenovo\Desktop\reader.txt","r")
a=f.read().split()
t=Turtle()
u=Turtle()
u.pu()
u.color('grey')
u.setpos(-200,0)
v=Turtle()
v.pu()
v.color('grey')
v.setpos(200,0)
t.ht()
u.ht()
v.ht()
i=0
d=Turtle()
d.pu()
d.shape("turtle")
d.setpos(200,0)
d.pd()
d.pensize(3)
d.lt(90)
d.fd(200)
d.bk(400)
d.fd(200)
d.pu()
d.shapesize(2,2)
def rewind():
    global i
    if i>30:
        i-=30
        time.sleep(0.2)
while i in range(0,len(a)):
    delay=0.2-d.ycor() *0.001
    t.write(a[i],align="center",font=("Arial",30,("bold","italic")))
    #if i>0:
        
    u.write(round(60*(1/delay)),align="center",font=("Arial",30,("bold","italic")))
   # if i<len(a):
     #   v.write(a[i+1],align="center",font=("Arial",30,("bold","italic")))

    listen()
    onkey(rewind,'space')
    if d.xcor != 200:
        d.setx(200)
    y=d.ycor()
    if y > 200:
        d.sety(200)
    if y <-200:
        d.sety(-200)
    d.ondrag(d.goto)
    #time.sleep(delay+(0.015*len(a[i])))
    time.sleep(delay)
    i+=1    
    t.clear()
    u.clear()
    v.clear()
    update()

