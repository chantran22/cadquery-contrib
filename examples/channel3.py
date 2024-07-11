import cadquery as cq

densc = 7850/1e9 #
(L, H, W, tw, tf) = (500.0, 120.0, 50.0, 5.0, 9.0)
L1=0.75*L

A1= H+40*2
B1= W+40*2
t = tf

pts = [
      (W/2, -H/2),
      (-W/2, -H/2),
      (-W/2, H/2),
      (W/2, H/2),
      (W/2, H/2-tf),
      (-W/2 +tw, H/2-tf),
      (-W/2 +tw, -H/2+tf),
      (W/2, -H/2+tf),
      (W/2, -H/2),

]

a= W-tw
b= H-2*tf
c=10
pts2 = [
      (a/2, 0),
      (-a/2+c, 0),
      (-a/2, c),
      (-a/2, b-c),
      (-a/2+c, b),
      (a/2, b),
]
r1 = (
      cq.Workplane("XY").polyline(pts).close().extrude(L)
     .copyWorkplane(cq.Workplane("XZ",origin=(0, L1/2, L+H/2)))
     .polyline(pts).close().extrude(L1)
)


st1 = (
         cq.Workplane("XZ").polyline(pts2).close().extrude(tw)
    ).translate((tw/2,H/2,L+tf))

st2= st1.mirror(mirrorPlane="XZ", basePointVector=(0, 0, 0))
Sp= st2.union(st1).union(r1)

base = (
    cq.Workplane("XY")
    .box(B1, A1, t)
    .faces(">Z")
    .workplane()
    .rect(B1-6*t, A1 -6*t, forConstruction=True)
    .vertices()
    .hole(16)
).translate((0,0,-tf/2))

#a= Sp.getVolume()*densc
show_object(Sp)
show_object(base)
#print(f"\nweight object = {a} kg") 
