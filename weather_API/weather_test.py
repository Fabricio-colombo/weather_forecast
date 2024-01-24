import requests
from tkinter import Tk, Label, Entry, Text, Button, CENTER

# link do open_weather: https://openweathermap.org/
API_KEY = "184fd29779e314cea46590e9c90bb957"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    link = f"{BASE_URL}?q={city}&appid={API_KEY}&lang=pt_br"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = round(requisicao_dic['main']['temp'] - 273.15, 1)
    return descricao, f"{temperatura}ºC"

def update_weather():
    city = city_entry.get()
    weather = get_weather(city)
    weather_text.delete(1.0, 'end')
    weather_text.insert('end', weather)

root = Tk()
root.geometry('400x300')
root.configure(bg='blue')
root.title('Previsão do tempo')

#criar um titulo para ficar dentro da interface, em cima do campo de texto chamado de Clima
title_label = Label(root, text="Informe sua Cidade", font=("Helvetica", 15), pady=10 , bg='blue', fg='white')
title_label.pack()

# Centralize a janela
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry("+{}+{}".format(position_right, position_down))

city_entry = Entry(root, font=('Arial', 14), fg='black', bg='white', borderwidth=2)
city_entry.pack(pady=10)

get_weather_button = Button(root, text="Obter clima", command=update_weather, padx=10, pady=10, bg='white', fg='blue')
get_weather_button.pack(pady=10)

weather_text = Text(root, height=1, font=("Helvetica", 15), pady=10, padx=10, bg='white', fg='darkblue')
weather_text.pack(pady=5)

root.mainloop()