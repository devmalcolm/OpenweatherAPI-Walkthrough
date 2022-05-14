# coding utf-8
import requests
from tkinter import *
import time
import os
import math
from PIL import ImageTk, Image

class get_weather():
    def __init__(self):
        # API KEY
        self.API_KEY = "4deca25b17dd74677fae9c530e322653"
        self.CITY_NAME = str(input("Choose A City: "))
        self.url = f" http://api.openweathermap.org/data/2.5/weather?q={self.CITY_NAME}&appid={self.API_KEY}"
        self.response = requests.get(self.url).json()
        self.temp_kelvin = self.response['main']['temp']
        self.feels_like = self.response['main']['feels_like']
        self.weather = self.response['weather'][0]['main']
        self.min_temp = self.response['main']['temp_min']
        self.max_temp = self.response['main']['temp_max']
        self.description = self.response['weather'][0]['description']

    def get_response(self):
        # Does not appear on the final output(Just for me)
        print(self.CITY_NAME)
        # print(self.feels_like)
        print(self.weather)
        print("Kelvin Temperature ", self.temp_kelvin)
        print("Feels Like Value ", self.feels_like)

    def kelvin_formula(self):
        # Fonction to convert our kelvin to celsius
        # Formule is: {Kelvin} - 273.15 = output_result
        celsius_cal = 273.15
        # The variable to calcul
        temp_celsius = self.temp_kelvin - celsius_cal
        feelslike_celsius = self.feels_like - celsius_cal
        # Feels Like K to C°
        min_temp = self.min_temp - celsius_cal
        max_temp = self.max_temp - celsius_cal
        # Math Floor Calcul
        max_temp_calcul = math.floor(max_temp)
        min_temp_calcul = math.floor(min_temp)
        feelslike_celsius_calcul = math.floor(feelslike_celsius)
        temp_celsius_calcul = math.floor(temp_celsius)
        # Median Calcul
        median_average_temp = max_temp_calcul + min_temp_calcul
        median_average_temp_calcul = median_average_temp / 2
        # Change function
        result_output_func = GW.result_output(
        max_temp_calcul, min_temp_calcul, feelslike_celsius_calcul, temp_celsius_calcul, median_average_temp_calcul)
        return result_output_func

    def result_output(self, max_temp_calcul, min_temp_calcul, feelslike_celsius_calcul, temp_celsius_calcul, median_average_temp_calcul):
        os.system('cls')
        print(f"Temperature of : {self.CITY_NAME}")
        print("Temperature in C° : ", temp_celsius_calcul, "°")
        print("Feels Like in C° : ", feelslike_celsius_calcul, "°")
        print("--")
        print("Current Minimum Temperature : ", min_temp_calcul, "°")
        print("Current Maximum Temperature : ", max_temp_calcul, "°")
        print("Median Temperature : ", median_average_temp_calcul, "°")
        print(self.response)
        print(self.description)

        tkinter_output_fun = GW.tkiner_UI(temp_celsius_calcul, feelslike_celsius_calcul)
        return tkinter_output_fun

    def tkiner_UI(self, temp_celsius_calcul, feelslike_celsius_calcul):
        app_root = Tk()
        app_root.title("Weather Application")
        app_root.config(bg = "white")
        app_root.iconbitmap("weathericon.ico")
        app_root.resizable(False, False)


        if self.description == 'few clouds':
            app_root_img = Image.open(r"giphy.gif")
            app_root_img = app_root_img.resize((150,150))
            app_root_img = ImageTk.PhotoImage(app_root_img)
            print('match')
        elif self.description == 'clear sky':
            app_root_img = Image.open(r"weatherimg.png")
            app_root_img = app_root_img.resize((150,150))
            app_root_img = ImageTk.PhotoImage(app_root_img)
        else:
            app_root_img = Image.open(r"weatherimg.png")
            app_root_img = app_root_img.resize((150,150))
            app_root_img = ImageTk.PhotoImage(app_root_img)
        
        LabelMain = Label(app_root,font=('Calibri bold', 20), bg="white")
        LabelMain.grid(row=0, sticky="N",padx=100)
        TempLabel = Label(app_root, font=("Calibri bold", 70), bg="white")
        TempLabel.grid(row=1, sticky="W", padx=50, pady=1)
        FeelLabel = Label(app_root,font=("Calibri bold", 15), bg="white")
        FeelLabel.grid(row=2,sticky="W", padx=10)

        Label(app_root, image=app_root_img,bg="white").grid(row=1,sticky="E")
        LabelMain.config(text="{}, {}".format(self.CITY_NAME, self.description))
        TempLabel.config(text="{}°".format(temp_celsius_calcul))
        FeelLabel.config(text="Feels Like Temperature : {}°".format(feelslike_celsius_calcul))
        #mostly cloud
        app_root.mainloop()


GW = get_weather()
GWRES = GW.kelvin_formula()
print(GWRES)
