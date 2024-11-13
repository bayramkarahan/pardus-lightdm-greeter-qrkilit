#!/usr/bin/python3
import gi
import os
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk
hesapkodu=None


class LabelWindow(Gtk.Window):

    def __init__(self):

        super().__init__(title="Qrkilit")
        global hesapkodu
        self.set_size_request(300,200)
        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        hbox.set_homogeneous(False)
        label = Gtk.Label(label="Hesap Kodu")
        hbox.pack_start(label, True, True, 0)
        
        hesapkodu=Gtk.Entry()
        hbox.pack_start(hesapkodu, True, True, 0)
        
        button = Gtk.Button(label="Kaydet")
        label.set_mnemonic_widget(button)
        button.connect("clicked",self.hesapkodukaydet_clicked)
        hbox.pack_start(button, True, True, 0)

        self.add(hbox)
        
    def hesapkodukaydet_clicked(self,button):
        global hesapkodu
        print(hesapkodu.get_text())
        os.system("echo 'kurumkod:"+hesapkodu.get_text()+"|:ebaqr' | netcat localhost 7777 &")
         


style_provider = Gtk.CssProvider()
css = open('/usr/share/pardus/pardus-lightdm-greeter/qrkilit.css', 'rb')
css_data = css.read()
css.close()
style_provider.load_from_data(css_data)
Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
window = LabelWindow()

window.connect("destroy", Gtk.main_quit)

window.show_all()

Gtk.main()
