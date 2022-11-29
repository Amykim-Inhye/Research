# turtle.py
# Challenge 1
# Author:Amy
# date: 10.11.22

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
