import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')    # Add a touch of color
# All the stuff inside your window.

layout = [  [sg.Text('Taschenrechner')],
            [sg.Text('Zahl1'), sg.InputText(), sg.Text('Zahl2'), sg.InputText()],
            [sg.Button('Summe')],
            [sg.Button('Produkt'),sg.Button('Differenz'), sg.Button('Quotient') ,
            sg.Button('Cancle')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break       #geht ans Ende der Schleife (verlässt die Schleife)
    #print('You entered ', values [0], values[1]), event)
    #print('Summe:', int(values[0]) + int(values[1]))
    try:
        z1= int(values[0])      # Zahl in ekigen Klammern index
        z2= int(values[1])
    except:
        print('Bitte nur Zahlen eingeben')
        sg.Popup('Bitte nur Zahlen eingeben')
        continue        # geht an den Anfangder Schleife
        
   
    if event=='Summe':
        print('Die Summe von {} und {} ist {}'. format(z1,z2,z1+z2))
    if event=='Produkt':
        print('Das Produkt von {} und {} ist {}'. format(z1,z2,z1*z2))
    if event=='Differenz':
        print ('Die Different von {} und {} ist {}'. format(z1,z2,z1-z2))
    if event=='Quotient':
        print ('Das Quotient von {} und {} ist {}'. format(z1,z2,z1/z2))
        

window.close()
