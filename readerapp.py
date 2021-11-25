from turtle import*
import time
tracer(0)

delay=0.05
f=open(r"C:\Users\Lenovo\spdreader\reader.txt","r")

#there is an automatic mode where the dealy is set by the length of the word

auto=False #make this true for auto mode
a=f.read().split() #makes a list of the text pasted
t=Turtle()
u=Turtle()
u.pu()
u.color('grey')
u.setpos(-200,0) #turtle graphics stetting up things
t.ht()
u.ht()
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
def rewind():       #rewinds by 30 words when space is pressed
    global i
    if i>30:
        i-=30
        time.sleep(0.2)  #delay for user to know its rewinded
while i in range(0,len(a)):
    delay=0.2-d.ycor() *0.001 #takes the y coordinate of the turtle on the right and changes delay accordingly
    t.write(a[i],align="center",font=("Arial",30,("bold","italic")))        
    u.write(round(60*(1/delay)),align="center",font=("Arial",30,("bold","italic")))

    listen()
    onkey(rewind,'space')
    if d.xcor != 200:
        d.setx(200)
    y=d.ycor()
    if y > 200:
        d.sety(200)          #this part is the wpm adjusting
    if y <-200:
        d.sety(-200)
    d.ondrag(d.goto)
    if auto==True:
        time.sleep(delay+(0.015*len(a[i]))) #dynamically changes delay word by word
    if auto==False:
        time.sleep(delay) 
    i+=1    
    t.clear()
    u.clear()

    update()

