import asyncio
import qrcode

ekilitpopover = None
ekilitimage = None
ekilittext = None
ekilitfile ="/tmp/qrekillit.png"

def _ekilitqrkod_button_event(widget=None):
    global random_label_text
    random_label_text=_("Loading...")
    #loginwindow.o("ui_popover_network").popup()
    os.system("rm /tmp/qrekillit.png")
    ekilitpopover.popup()
    ekilitqrcode_control_event()

random_label_text=""
_last_random_label_text=""
def update_popover_ekilit_text():
    global _last_random_label_text
    if _last_random_label_text != random_label_text:
        _last_random_label_text = random_label_text
        ekilittext.set_text(random_label_text)
        img = qrcode.make(random_label_text)
        #ekilittext.set_text(lan_ip.strip())
        img.save(ekilitfile)
        ekilitimage.set_from_file(ekilitfile)       
    GLib.timeout_add(500,update_popover_ekilit_text)

@asynchronous
def ekilitqrcode_control_event():
    global random_label_text
    random_label_text=random.randrange(100000, 999999)

def module_init():
    #if not get("show-widget",True,"network"):
        #loginwindow.o("ui_button_network").hide()
    global ekilitpopover
    global ekilitimage
    global ekilittext
    #if os.path.isfile(ekilitfile):
        #os.unlink(ekilitfile)
    ekilitpopover = Gtk.Popover()
    ekilitimage = Gtk.Image()
    ekilittext = Gtk.Label()
    b = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    b.pack_start(ekilitimage,False,False,0)
    b.pack_start(ekilittext,False,False,0)
    ekilitpopover.add(b)
    ekilitpopover.set_position(Gtk.PositionType.BOTTOM)
    button = Gtk.MenuButton(label="E-KİLİT", popover=ekilitpopover)
    button.connect("clicked",_ekilitqrkod_button_event)
    loginwindow.o("ui_box_bottom_left").pack_end(button, False, True, 10)
    button.get_style_context().add_class("icon")
    button.show_all()
    b.show_all()
    #loginwindow.o("ui_button_network").connect("clicked",_ekilitqrkod_button_event)
    update_popover_ekilit_text()

