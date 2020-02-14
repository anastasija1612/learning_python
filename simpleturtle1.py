import PySimpleGUI as sg
import turtle

def snowman(basis=50, ecken=None):
    #---bauch beginnt am fuß, schaut nach rechts
    rosi.begin_fill()
    rosi.circle(basis, steps=ecken)
    rosi.end_fill()
    #--rauf zum kopf
    rosi.penup()
    rosi.circle(basis, 180) #schaut jetzt nach links
    rosi.pendown()
    rosi.begin_fill()
    rosi.circle(-basis//2, steps=ecken)  #// division ohne rest
    rosi.end_fill()
    # rosi soll am startpunkt zurück
    rosi.penup()
    rosi.circle(basis,180)
    rosi.pendown()
 
 
 
def make_snowman():
        #----checkem ob im Backgroundcolor eine vernünftige Farbe drinnen steht
        try:
            rosi.fillcolor(values["bv"])
        except:
            rosi.fillcolor ("#000000") #schwarz geht immer als füllfarbe 
        #----check Pencolor
        try: 
            rosi.pencolor(values["cv"])
        except:
            rosi.pencolor("#ff0000")    #na dann halt rot
        #----check pensize----
        try:
            rosi.pensize(values["sv"])
        except:
            rosi.pensize(1) #strichstärke 1 wenn in sv ein unsinnn steht
        #---nimm das feld grad für die anzhal der ecken---
        
        try:
            snowman(int(values["fv"]), int(values["rv"]))   #nimm das feld Weie für schneemanngröße 
        except:
            snowman()
    
layout = [[sg.Text("Mein Wurfssimulator")],
          [sg.Text("Weite:"), sg.Input(key="fv", default_text=20),
           sg.Text("Grad:"), sg.Input(key="rv", default_text=15)],
          [ sg.Text("Farbe:"), sg.Input(key="cv", default_text="#ff0000"),
          sg.Text("Backgroundcolor:"), sg.Input(key="bv", default_text="#ff0000")],
           [sg.Text("Dicke:"), sg.Input(key="sv", default_text=1)],
          [sg.Canvas(size=(900, 600), key="sandbox")],
          [sg.Button("vorwärts"), sg.Button("links"), sg.Button("rechts")],
          [sg.Button("clear"),sg.Button("Home"), sg.Button("penup"), sg.Button("pendown"),
          sg.Button("Snowman"), sg.Button("Schneemannplanet")],
          ]
        

window= sg.Window("My window", layout, finalize=True)
canvas = window ["sandbox"].TKCanvas

rosi=turtle.RawTurtle(canvas)
rosi.pencolor("#ff0000") #Red
rosi.shape("turtle")
#rosi.speed =20
rosi_dreh=15
while True:         # Event Loop
    event, values =window.read()
    if event is None:
        break
     #---inputs---
     #----buttons----
    if event =="clear":
        rosi.clear()
    if event =="Home":
        rosi.home()
    if event =="penup":
        rosi.penup()
    if event =="pendown":
        rosi.pendown()
        
    if event == "vorwärts" :
        #raw= values["sv"]
        try:
            rosi.pensize (values["sv"])
        except:
            rosi.pensize (1)
        rc= values ["cv"]
        #set the pen color
        try:
            rosi.pencolor(rc)
        except:
            rosi.pencolor("#ff0000")
        #set background color
       # bc=values["bv"]
      #  try:
        #   rosi.backgroundcolor(bc)
        #except:
        #   canvas.backgroundcolor
        raw = values["fv"]
        try:
            raw=int(raw)
        except:
            raw=20
        rosi.forward(raw)
    
        
    elif event == "links":
        raw=values["rv"]
        try:
            raw=int(raw)
        except:
            raw=20
        rosi.left (raw)
        
    elif event == "rechts":
        raw=values["rv"]
        try:
            raw=int(raw)
        except:
            raw=20
        rosi.right(raw)
    elif event == "Snowman":
      make_snowman()
    elif event == "Schneemannplanet":
        for x in range(10):
            make_snowman()
            rosi.right(360/10)
      
window.close()
