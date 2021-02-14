import tkinter as tk
from tkinter import font
import requests




HEIGTH = 700
WIDTH = 800

def test_function(dood):
    print("This is what was entered", dood)

#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
# 042f6c06d5410a3eac412c958bdc3e3d

def format_response(weather):
    print(weather)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
    
        #percent string to 
        final_string = "City: %s \nCondition: %s \nTemperature (*F): %s" % (name, desc, temp)
    except:
        final_string = "There was a problem retrieving that info"

    return final_string
def get_weather(city):
    weather_key = '042f6c06d5410a3eac412c958bdc3e3d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    lebel['text'] = format_response(weather)
    

root = tk.Tk()

canvas = tk.Canvas(root,height=HEIGTH,width=WIDTH)
canvas.pack() #pack() draws object to the screen(gui)

#makes an image and 
backgroud_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=backgroud_image)
background_label.place(relwidth=1, relheight=1)

#places object on a percent of the screen
#and wont move from that spicific spot on the screen (relx and rely)
frame = tk.Frame(root,bg = "purple",bd=5) #bd is the border size
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = .1, anchor = "n")  

entry = tk.Entry(frame, font= 40) #draws object inside the frame
entry.place(relwidth = 0.65, relheight = 1)  
                                                                #takes input from entry and puts in the the test_function()
button = tk.Button(frame,bg = "blue",text="Text button", font = 40,command=lambda:get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)     #lambda gets info from function updates input


lower_frame = tk.Frame(root, bg ="purple", bd = 10)
lower_frame.place(relx = 0.50, rely =0.25, relwidth = 0.75, relheight=0.6, anchor= "n" )

lebel = tk.Label(lower_frame, text="This is a label", bg="yellow", font=('Lato', 20), anchor='nw', justify='left')
lebel.place(relwidth=1, relheight=1)

# lebel = tk.Label(frame, text = "Hello World", bg="yellow")
# lebel.grid(row = 1, column = 0)

# shows all the fonts in the tkinter library
# print(tk.font.families())




root.mainloop()