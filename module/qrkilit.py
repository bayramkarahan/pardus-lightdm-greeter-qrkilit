import asyncio
import qrcode
import random

qrkilitpopover = None
qrkilitimage = None
qrkilittext = None
qrkilitfile ="/tmp/qrekillit.png"
qrkilitinput= None
random_label_text=""
_last_random_label_text=""
result_pass_str=""

def _qrkilitqrkod_button_event(widget=None):
    global random_label_text
    random_label_text=_("Loading...")
    #loginwindow.o("ui_popover_network").popup()
    os.system("rm /tmp/qrekillit.png")
    qrkilitpopover.popup()
    qrkilitqrcode_control_event()


def update_popover_qrkilit_text():
    global _last_random_label_text
    global result_pass_str
    if _last_random_label_text != random_label_text:
        _last_random_label_text = random_label_text
        qrkilittext.set_text("qrkilit sistemi")
        img = qrcode.make(random_label_text)
        #qrkilittext.set_text(lan_ip.strip())
        img.save(qrkilitfile)
        qrkilitimage.set_from_file(qrkilitfile)       
    GLib.timeout_add(500,update_popover_qrkilit_text)

@asynchronous
def qrkilitqrcode_control_event():
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

def loginqrkilitbutton_clicked(button):
    global qrkilitpopover
    global result_pass_str
    
    if qrkilitinput.get_text() == result_pass_str:
        #print(random_label_text)
        qrkilitpopover.hide()
        print("giriş yapılıyor..")
        os.system("echo 'ebaqrebaqr:ebaqr:ebaqr' | netcat localhost 7777 &")
    

def module_init():
    global qrkilitpopover
    global qrkilitimage
    global qrkilittext
    global qrkilitinput
    global loginqrkilitbutton
    qrkilitpopover = Gtk.Popover()
    qrkilitimage = Gtk.Image()
    qrkilittext = Gtk.Label()
    qrkilitinput=Gtk.Entry()
    loginqrkilitbutton = Gtk.Button.new_with_label("Giriş")
    loginqrkilitbutton.connect("clicked",loginqrkilitbutton_clicked)
    b = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    b.pack_start(qrkilitimage,False,False,0)
    
    b.pack_start(qrkilittext,False,False,0)
    b.pack_start(qrkilitinput,False,False,0)
    b.pack_start(loginqrkilitbutton,False,False,0)

    qrkilitpopover.add(b)
    qrkilitpopover.set_position(Gtk.PositionType.BOTTOM)
    button = Gtk.MenuButton(label="QRKILIT", popover=qrkilitpopover)
    button.connect("clicked",_qrkilitqrkod_button_event)
    loginwindow.o("ui_box_bottom_left").pack_end(button, False, True, 10)
    button.get_style_context().add_class("icon")
    button.show_all()
    b.show_all()
    #loginwindow.o("ui_button_network").connect("clicked",_qrkilitqrkod_button_event)
    update_popover_qrkilit_text()
