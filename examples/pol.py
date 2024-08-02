from cadquery import *
#from cadquery.selectors import *
from math import cos, radians, sqrt, sin

#--------
def pol_points(radius, num_points):
    points = []
    ang= 360/num_points
    beta= ang/2
    for i in range(0, num_points):
        rad = radians(ang*i+ beta)
        x = radius * cos(rad)
        y = radius * sin(rad)
        points.append((x, y))
    return points

#________


n,a= 8,1600
b= a-100
h=150

ang= 360/8/2
l= a/2*cos(radians(ang))
w= sqrt((a/2)**2 + l**2)

wp= cq.Workplane('XY')
wp1= cq.Workplane('YZ')

s1= wp.polygon(n,a).polygon(n,b).extrude(h)
#s1= wp.polygon(n,a).offset2D(-50).extrude(h)
s1= s1.shell(-4).rotate((0,0,0),(0,0,1),ang)

b1= wp1.rect(50,h).extrude(l*2-80).translate((-l+40,w/4,h/2))
b1= b1.faces(">X" and "X").shell(-4)
b2= b1.mirror(mirrorPlane="XZ", basePointVector=(0, 0, 0))

gb1= b1.union(b2)
gb2= gb1.rotate((0,0,0),(0,0,1),90)

base= gb1.union(gb2).union(s1)
pts= pol_points((a-150)/2,8)
#legs= wp.pushPoints(pts).rect(50,h).extrude(-300)
#legs= legs.rotate((0,0,0),(0,0,1),ang)

pts1= [(w/4,(a-270)/2), (-w/4,(a-270)/2),
       (w/4,-(a-270)/2), (-w/4,-(a-270)/2)]

leg1= wp.pushPoints(pts1).rect(50,h).rect(42,h-8).extrude(-410)
leg2= leg1.rotate((0,0,0),(0,0,1),90)

legs= leg1.union(leg2)

show_object(base)
show_object(legs)
#show_object(gb2)

