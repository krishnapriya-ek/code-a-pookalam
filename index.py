# outer_circle
c = circle(r=150,fill="darkgreen",stroke="black",stroke_width=2)
show(c)
# inner_two_circles
circle1=circle(r=140,fill="yellow",stroke="none",)
circle2=circle(r=130,fill="lightgreen",stroke="none",)
show(circle1,circle2)
# inner_squares
a=rectangle(w=210,h=210,fill="red",stroke="black",stroke_width=2) |repeat(6,rotate(30)) 
show(a)
#inner_squaresss
a1=rectangle(w=200,h=200,fill="white",stroke="black",)| repeat(20,rotate(20))
a2=rectangle(w=190,h=190,fill="yellow",stroke="none",) |repeat(20,rotate(20))
a3=rectangle(w=180,h=180,fill="orange",stroke="none",) |repeat(20,rotate(20))
a4=rectangle(w=170,h=170,fill="red",stroke="none",) |repeat(20,rotate(20))
a5=rectangle(w=160,h=160,fill="brown",stroke="none",) |repeat(20,rotate(20))
show(a1,a2,a3,a4,a5)
# ovals
q1=ellipse(w=200,h=100,fill="yellow",stroke="none") | repeat(6,rotate(30))
q2=ellipse(w=190,h=90,fill="violet",stroke="none")|repeat(6,rotate(30))
q3=ellipse(w=180,h=80,fill="blue",stroke="none") | repeat(6,rotate(30))
show(q1,q2,q3)
#squares
h1=rectangle(w=110,h=110,fill="black",stroke="none") | repeat(6,rotate(30))
h2=rectangle(w=100,h=100,fill="brown",stroke="none") | repeat(6,rotate(30))
h3=rectangle(w=90,h=90,fill="red",stroke="none") | repeat(6,rotate(30))
h4=rectangle(w=80,h=80,fill="orange",stroke="none") | repeat(6,rotate(30))
h5=rectangle(w=70,h=70,fill="yellow",stroke="none") | repeat(6,rotate(30))
h6=rectangle(w=60,h=60,fill="white",stroke="none") | repeat(6,rotate(30))
show(h1,h2,h3,h4,h5,h6)
# circles
j1=circle(r=50,fill="green",stroke="none")
j2=circle(r=40,fill="orange",stroke="none")

show(j1,j2)
#oval
t1=ellipse(w=80,h=40,fill="blue",stroke="none")|repeat(6,rotate(30))
t2=ellipse(w=70,h=60,fill="violet",stroke="none")|repeat(6,rotate(30))
t3=ellipse(w=60,h=50,fill="yellow",stroke="none")|repeat(6,rotate(30))
show(t1,t2,t3)
#circles
f1=circle(r=20,fill="orange",stroke="none")
f2=circle(r=10,fill="red",stroke="none")
show(f1,f2)


    
          

