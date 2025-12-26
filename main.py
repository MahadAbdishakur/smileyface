# Write your code here :-)
print("hello world")
import turtle #allows us to use this libary or added program or something, note to self, learn the name
screen = turtle.Screen() #im assuming this sets up the screen
screen.title("Smiling Face with Python Turtle") #title of the image im assuming
t = turtle.Turtle() #makes it easier to call turtle which is the funny libary name
t.speed(8) #dictates the speed of the drawing, may or may not be what decides the speed of each item and not just this one circle
t.penup() #i dont know what this does ??
t.goto(0, -100) #im asssuming this is the reason why its sorta in the middle, when changed to a postive number it moves higher up in the screen
t.pendown() #ik its self explantory but how does it work and what function is this exactly
t.color("yellow") # color picker
t.begin_fill() #filler 
t.circle(100) #shape 
t.end_fill()# it picked a color, began to fill and picked a shape and ended fill
#left eye
t.penup()
t.goto(-40, 20 ) # im assuming the right eye will be the opposite (40, -20) which might not make sense, it will probaly be postive 20 and positive 40
t.pendown #WHAT DOES THIS DOOO
t.color("black") #WHATEVER WE ALREADY KNOW
t.begin_fill() #IK WHAT THIS DOES WHY ARE WE REITERATING, IK ITS FOR PRATICE BUT CHILL 
t.circle(15) #A CIRCLE LIKE WHAT BUT THE 15 IS INTRESTING <COULD BE WRONG
t.end_fill() ##
#righteye
t.penup() #still dont know
t.goto(40, 20) # I WAS FUCKIN RIGHT
t.pendown() #still dont know
t.begin_fill() #after we create the shape by carving it out then we begin fill
t.circle(15) # this makes a circle but idk what the point of the goto is for
t.end_fill()
#  the cursor is called a turtle
#frown
t.penup()
t.goto(40, -20) # wow i think this goes from one eye to the other
t.pendown() #idk okay
t.width(8) # this is how thick the smile is
t.color("black") #black the color
t.setheading(-60) #the angle i think
t.circle(-50, -120) #what made it a frown an upsided down smile
#mad
#confused
#smile

#   t.penup()
#  t.goto(-40, -20) # wow i think this goes from one eye to the other
#  t.pendown() #idk okay
#  t.width(8) # this is how thick the smile is
#  t.color("black") #black the color
#  t.setheading(-60) #the angle i think
#  t.circle(50, 120) #wtf
# extra steps for prettiness
t.hideturtle #hides cursor
screen.mainloop() #i think this closes the drawing and keeps the window open
#if turtle is True :
 #   print("works")
#else:
  #  print("false")