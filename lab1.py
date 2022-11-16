import math
x1=22 #точне число sqrt(x1 )
x2=2/21 #точне число x2
x1_1=4.69 #наближене число x1
x2_2=0.095 #наближене число x2
def f(x1, x1_1, x2, x2_2):
    dx1=abs((math.sqrt(x1)-x1_1)/math.sqrt(x1))
    dx2 = abs((x2-x2_2)/x2)
    if (dx1>dx2):
        print ("Друга рівність точніше")
    else:
        print("Перша рівність точніше")
f(x1,x1_1,x2,x2_2)
