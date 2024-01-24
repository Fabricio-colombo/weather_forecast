import requests
from tkinter import Tk, Label, Entry, Text, Button
from PIL import Image, ImageTk

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
root.geometry('400x600')
root.configure(bg='blue')
root.title('Previsão do tempo')

# Colocar a imagem superior.png na parte de cima da interface
imagem_superior = Image.open('weather_API/imagens/superior.png')
imagem_superior = ImageTk.PhotoImage(imagem_superior)

# Criar um rótulo para exibir a imagem na interface
label_imagem_superior = Label(root, image=imagem_superior, bg='blue')
label_imagem_superior.pack()

# Criar um título para ficar dentro da interface, em cima do campo de texto chamado de Clima
title_label = Label(root, text="Informe sua Cidade", font=("Arial", 20, "bold"), pady=10, bg='blue', fg='white')
title_label.pack()

# Impedir que o usuário redimensione a janela
root.resizable(False, False)

# Centralizar a janela com ajuste fino
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2.5 - window_width / 6)
position_down = int(root.winfo_screenheight() / 4 - window_height / 4) - 60  # Ajuste fino para cima
root.geometry("+{}+{}".format(position_right, position_down))



city_entry = Entry(root, font=('Arial', 14), fg='black', bg='#E0E0E0', borderwidth=2, relief='solid', width=20)
city_entry.pack(pady=10)

get_weather_button = Button(root, text="Obter Clima", command=update_weather, font=('Arial', 14, 'bold'), padx=15, pady=10, bg='#3498db', fg='white', borderwidth=2, relief='solid')
get_weather_button.pack(pady=10)

weather_text = Text(root, height=1, font=("Arial", 15), pady=10, padx=10, bg='#E0E0E0', fg='darkblue', borderwidth=2, relief='solid', highlightbackground='gold', width=18)
weather_text.pack(pady=5)

root.mainloop()
