import gi
import datetime
import requests

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

class AlwaysOnTopWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="💵 Dólar Blue 💵")
        self.set_default_size(200, 90)

        # Configurar la ventana para que sea siempre visible
        self.set_keep_above(True)
        self.set_type_hint(Gdk.WindowTypeHint.DIALOG)

        # Crear un contenedor vertical para las etiquetas
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Crear una etiqueta para mostrar el valor del dólar blue
        self.label = Gtk.Label(label="Cargando...")
        self.label.set_margin_top(5)
        box.pack_start(self.label, False, False, 0)

        # Crear una etiqueta para mostrar la hora de la última actualización
        self.timestamp_label = Gtk.Label(label="")
        self.timestamp_label.set_margin_top(4)
        box.pack_start(self.timestamp_label, False, False, 0)

        # Obtener el valor del dólar blue
        self.fetch_data()

        # Actualizar los datos cada 5 minutos
        GLib.timeout_add_seconds(30, self.fetch_data)

        # Crear una etiqueta adicional para el texto personalizado
        self.additional_label = Gtk.Label(label="Hecho con ❤️ por SantiagoSito")
        self.additional_label.set_margin_top(4)
        self.additional_label.set_margin_bottom(1)
        self.additional_label.set_margin_left(1)
        self.additional_label.set_margin_right(1)
        box.pack_start(self.additional_label, False, False, 0)

    def fetch_data(self):
        try:
            # Realizar la solicitud a la API para obtener los datos del dólar blue
            url = "https://api.bluelytics.com.ar/v2/latest"
            response = requests.get(url)
            data = response.json()
            sell_amount = data["blue"]["value_sell"]
            buy_amount = data["blue"]["value_buy"]

            # Actualizar la etiqueta con los valores del dólar blue
            self.label.set_label(f"Compra: {buy_amount} - Venta: {sell_amount}")

            # Obtener la hora actual y mostrarla como la hora de la última actualización
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.timestamp_label.set_label(f"Última actualización: {current_time}")
        except Exception as e:
            self.label.set_label("Error al obtener los datos")

        # Retornar True para seguir actualizando los datos
        return True

win = AlwaysOnTopWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()