from tkinter import *

import tkintermapview


polcon:list=[]
artist:list=[]
worker:list=[]
temporary:list=[]

class temporarys:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

def create_artist():

    for idx,val in enumerate(temporary):
        temporary[idx].marker.delete()

    for idx,val in enumerate(worker):
        worker[idx].marker.delete()

    temporary.clear()
    u=listbox_lista_obiketow.index(ACTIVE)
    d=polcon[u].name

    for idx,val in enumerate(artist):
        if artist[idx].location2==d:
            val=temporarys(name=artist[idx].name,location=artist[idx].location)
            temporary.append(val)
        artist[idx].marker.delete()


    show_artist_temp()
    button_pokaz_szczegoly_obiektu_artist.configure(command=show_artist_temp_details)

def show_artist_temp():
    listbox_lista_artist.delete(0,END)
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,val in enumerate(temporary):
        listbox_lista_artist.insert(idx,f'{idx+1}.{val.name}')

def show_artist_temp_details():
    o=listbox_lista_artist.index(ACTIVE)
    name=temporary[o].name
    location=temporary[o].location

    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')

    map_widget.set_position(temporary[o].coordinates[0],temporary[o].coordinates[1])
    map_widget.set_zoom(17)


def create_workers():
    for idx, val in enumerate(temporary):
        temporary[idx].marker.delete()

    for idx,val in enumerate(artist):
        artist[idx].marker.delete()

    temporary.clear()
    u = listbox_lista_obiketow.index(ACTIVE)
    d = polcon[u].name

    for idx, val in enumerate(worker):
        if worker[idx].location2 == d:
            val = temporarys(name=worker[idx].name, location=worker[idx].location)
            temporary.append(val)

        worker[idx].marker.delete()

    show_worker_temp()
    button_pokaz_szczegoly_obiektu_worker.configure(command=show_worker_temp_details)


def show_worker_temp():
    listbox_lista_artist.delete(0, END)
    listbox_lista_obiektow_worker.delete(0, END)
    for idx, val in enumerate(temporary):
        listbox_lista_obiektow_worker.insert(idx, f'{idx + 1}.{val.name}')


def show_worker_temp_details():
    o = listbox_lista_obiektow_worker.index(ACTIVE)
    name = temporary[o].name
    location = temporary[o].location

    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')

    map_widget.set_position(temporary[o].coordinates[0], temporary[o].coordinates[1])
    map_widget.set_zoom(17)

def restore():
    show_artist()
    show_worker()
    for idx,val in enumerate(temporary):
        temporary[idx].marker.delete()

    for idx,val in enumerate(artist):
        artist[idx].coordinates=artist[idx].get_coordinates()
        artist[idx].marker=map_widget.set_marker(artist[idx].coordinates[0],artist[idx].coordinates[1])

    for idx,val in enumerate(worker):
        worker[idx].coordinates=worker[idx].get_coordinates()
        worker[idx].marker=map_widget.set_marker(worker[idx].coordinates[0],worker[idx].coordinates[1])

    button_pokaz_szczegoly_obiektu_worker.configure(command=show_worker_details)
    button_pokaz_szczegoly_obiektu_artist.configure(command=show_artist_details)




class Polcon:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

def add_polcon():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    user= Polcon(name=zmienna_imie, location=zmienna_miejscowosc)
    polcon.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_polcon()



def show_polcon():
    listbox_lista_obiketow.delete(0,END)
    for idx,user in enumerate(polcon):
        listbox_lista_obiketow.insert(idx,f'{idx+1}. {user.name}')


def remove_polcon():
    i=listbox_lista_obiketow.index(ACTIVE)
    polcon[i].marker.delete()
    polcon.pop(i)
    show_polcon()

def edit_polcon():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=polcon[i].name
    location=polcon[i].location

    entry_name.insert(0,name)
    entry_location.insert(0,location)

    button_dodaj_wydarzenie.config(text='zapisz',command=lambda: update_polcon(i))

def update_polcon(i):
    new_name=entry_name.get()
    new_location=entry_location.get()

    polcon[i].name=new_name
    polcon[i].location=new_location

    polcon[i].marker.delete()
    polcon[i].coordinates=polcon[i].get_coordinates()
    polcon[i].marker=map_widget.set_marker(polcon[i].coordinates[0],polcon[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_wydarzenie.config(text='Dodaj obiekt',command=add_polcon)
    show_polcon()


def show_polcon_workers():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=polcon[i].name
    location=polcon[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_workers()

    map_widget.set_position(polcon[i].coordinates[0],polcon[i].coordinates[1])
    map_widget.set_zoom(17)

def show_polcon_artist():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=polcon[i].name
    location=polcon[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_artist()

    map_widget.set_position(polcon[i].coordinates[0],polcon[i].coordinates[1])
    map_widget.set_zoom(17)




class Artist():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]


def add_artist():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_wydarzenie=entry_location2.get()
    user= Artist(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_wydarzenie)
    artist.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_artist()



def show_artist():
    listbox_lista_artist.delete(0,END)
    for idx,user in enumerate(artist):
        listbox_lista_artist.insert(idx,f'{idx+1}. {user.name}')

def remove_artist():
    i=listbox_lista_artist.index(ACTIVE)
    artist[i].marker.delete()
    artist.pop(i)
    show_artist()

def edit_artist():
    i=listbox_lista_artist.index(ACTIVE)
    name=artist[i].name
    location=artist[i].location
    location2=artist[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_artist.config(text='Zapisz',command=lambda: update_artist(i))

def update_artist(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    artist[i].name=new_name
    artist[i].location=new_location
    artist[i].location2=new_location2

    artist[i].marker.delete()
    artist[i].coordinates=artist[i].get_coordinates()
    artist[i].marker=map_widget.set_marker(artist[i].coordinates[0],artist[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_artist.config(text='Dodaj obiekt',command=add_artist)
    show_artist()


def show_artist_details():
    i=listbox_lista_artist.index(ACTIVE)
    name=artist[i].name
    location=artist[i].location
    location2=artist[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(artist[i].coordinates[0],artist[i].coordinates[1])
    map_widget.set_zoom(17)



class workers():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
         import requests
         from bs4 import BeautifulSoup
         url = f"https://pl.wikipedia.org/wiki/{self.location}"
         response = requests.get(url).text
         response_html = BeautifulSoup(response, "html.parser")
         longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
         latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
         print(longitude)
         print(latitude)
         return [latitude, longitude]

def add_worker():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_wydarzenie=entry_location2.get()
    user= workers(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_wydarzenie)
    worker.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_worker()



def show_worker():
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,user in enumerate(worker):
        listbox_lista_obiektow_worker.insert(idx,f'{idx+1}. {user.name}')


def remove_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    worker[i].marker.delete()
    worker.pop(i)
    show_worker()

def edit_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_worker.config(text='zapisz',command=lambda: update_worker(i))

def update_worker(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    worker[i].name=new_name
    worker[i].location=new_location
    worker[i].location2=new_location2

    worker[i].marker.delete()
    worker[i].coordinates=worker[i].get_coordinates()
    worker[i].marker=map_widget.set_marker(worker[i].coordinates[0],worker[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_worker.config(text='Dodaj obiekt',command=add_polcon)
    show_polcon()


def show_worker_details():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(worker[i].coordinates[0],worker[i].coordinates[1])
    map_widget.set_zoom(17)








root = Tk()
root.geometry("1200x760")
root.title("Project POP KB")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista wydarzeń")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiketow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiketow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż artystów', command=show_polcon_artist)
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż pracowników', command=show_polcon_workers)
button_pokaz_szczegoly_obiektu.grid(row=3, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_polcon)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_polcon)
button_edytuj_obiekt.grid(row=2, column=2)


label_lista_obiektow_artist=Label(ramka_lista_obiektow, text="Lista artystów")
label_lista_obiektow_artist.grid(row=0, column=3,columnspan=2)
listbox_lista_artist=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_artist.grid(row=1, column=3, columnspan=3)
button_pokaz_szczegoly_obiektu_artist=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_artist_details)
button_pokaz_szczegoly_obiektu_artist.grid(row=2, column=3)
button_usun_obiekt_artist=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_artist)
button_usun_obiekt_artist.grid(row=2, column=4)
button_edytuj_obiekt_artist=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_artist)
button_edytuj_obiekt_artist.grid(row=2, column=5)

label_lista_obiektow_worker=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_worker.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_worker=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_worker.grid(row=1, column=6, columnspan=3)
button_pokaz_szczegoly_obiektu_worker=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_worker_details)
button_pokaz_szczegoly_obiektu_worker.grid(row=2, column=6)
button_usun_obiekt_worker=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_worker)
button_usun_obiekt_worker.grid(row=2, column=7)
button_edytuj_obiekt_worker=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_worker)
button_edytuj_obiekt_worker.grid(row=2, column=8)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Nazwa:")
label_name.grid(row=1, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=2, column=0,sticky=W)
label_location2=Label(ramka_formularz, text="Wydarzenie:")
label_location2.grid(row=3, column=0,sticky=W)

entry_name=Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=2, column=1)
entry_location2=Entry(ramka_formularz)
entry_location2.grid(row=3, column=1)

button_dodaj_wydarzenie=Button(ramka_formularz, text='Dodaj wydarzenie',command=add_polcon)
button_dodaj_wydarzenie.grid(row=5, column=0, columnspan=2)

button_dodaj_artist=Button(ramka_formularz, text='Dodaj artystę',command=add_artist)
button_dodaj_artist.grid(row=6, column=0, columnspan=2)

button_dodaj_worker=Button(ramka_formularz, text='Dodaj pracownika',command=add_worker)
button_dodaj_worker.grid(row=7, column=0, columnspan=2)

button_odswiez=Button(ramka_formularz,text='Odśwież listę',command=restore)
button_odswiez.grid(row=8, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegoly obiektu:")
label_szczegoly_obiektow.grid(row=1, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Nazwa:")
label_szczegoly_name.grid(row=1, column=1)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=2)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=3)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=4)
label_szczegoly_location2=Label(ramka_szczegoly_obiektow, text="Wydarzenie:")
label_szczegoly_location2.grid(row=1, column=5)
label_szczegoly_location2_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location2_wartosc.grid(row=1, column=6)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()