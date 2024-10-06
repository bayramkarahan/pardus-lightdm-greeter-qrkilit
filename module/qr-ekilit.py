import asyncio
import qrcode
import random

ekilitpopover = None
ekilitimage = None
ekilittext = None
ekilitfile ="/tmp/qrekillit.png"
ekilitinput= None
random_label_text=""
_last_random_label_text=""
result_pass_str=""

def _ekilitqrkod_button_event(widget=None):
    global random_label_text
    random_label_text=_("Loading...")
    #loginwindow.o("ui_popover_network").popup()
    os.system("rm /tmp/qrekillit.png")
    ekilitpopover.popup()
    ekilitqrcode_control_event()


def update_popover_ekilit_text():
    global _last_random_label_text
    global result_pass_str
    if _last_random_label_text != random_label_text:
        _last_random_label_text = random_label_text
        ekilittext.set_text("ekilit sistemi")
        img = qrcode.make(random_label_text)
        #ekilittext.set_text(lan_ip.strip())
        img.save(ekilitfile)
        ekilitimage.set_from_file(ekilitfile)       
    GLib.timeout_add(500,update_popover_ekilit_text)

@asynchronous
def ekilitqrcode_control_event():
    global random_label_text
    global result_pass_str
    random_label_text=str(random.randrange(100000, 999999))
    p1=random_label_text[0]
    p2=random_label_text[1]
    p3=random_label_text[2]
    p4=random_label_text[3]
    p5=random_label_text[4]
    p6=random_label_text[5]
    #print(ps)
    #------------------
    p1=str(abs(((int(p1)+int(p1))-int(p2))*int(p3)))
    p2=str(abs(((int(p2)+int(p1))-int(p2))*int(p3)))
    p3=str(abs(((int(p3)+int(p1))-int(p2))*int(p3)))
    p4=str(abs(((int(p4)+int(p1))-int(p2))*int(p3)))
    p5=str(abs(((int(p5)+int(p1))-int(p2))*int(p3)))
    p6=str(abs(((int(p6)+int(p1))-int(p2))*int(p3)))
    result_pass_str=str(p1[0]+p2[0]+p3[0]+p4[0]+p5[0]+p6[0])

def loginekilitbutton_clicked(button):
    global ekilitpopover
    global result_pass_str
    
    if ekilitinput.get_text() == result_pass_str:
        #print(random_label_text)
        ekilitpopover.hide()
        print("giriş yapılıyor..")
        os.system("echo 'ebaqrebaqr:ebaqr:ebaqr' | netcat localhost 7777 &")
    

def module_init():
    global ekilitpopover
    global ekilitimage
    global ekilittext
    global ekilitinput
    global loginekilitbutton
    ekilitpopover = Gtk.Popover()
    ekilitimage = Gtk.Image()
    ekilittext = Gtk.Label()
    ekilitinput=Gtk.Entry()
    loginekilitbutton = Gtk.Button.new_with_label("Giriş")
    loginekilitbutton.connect("clicked",loginekilitbutton_clicked)
    b = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    b.pack_start(ekilitimage,False,False,0)
    
    b.pack_start(ekilittext,False,False,0)
    b.pack_start(ekilitinput,False,False,0)
    b.pack_start(loginekilitbutton,False,False,0)

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
