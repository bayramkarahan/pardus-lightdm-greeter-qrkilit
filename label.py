import gi


gi.require_version("Gtk", "3.0")

from gi.repository import Gtk



class LabelWindow(Gtk.Window):

    def __init__(self):

        super().__init__(title="Label Example")


        hbox = Gtk.Box(spacing=10)

        hbox.set_homogeneous(False)

        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        vbox_left.set_homogeneous(False)

        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        vbox_right.set_homogeneous(False)


        hbox.pack_start(vbox_left, True, True, 0)

        hbox.pack_start(vbox_right, True, True, 0)


        label = Gtk.Label(label="This is a normal label")

        vbox_left.pack_start(label, True, True, 0)


        label = Gtk.Label()

        label.set_text("This is a left-justified label.\nWith multiple lines.")

        label.set_justify(Gtk.Justification.LEFT)

        vbox_left.pack_start(label, True, True, 0)


        label = Gtk.Label(

            label="This is a right-justified label.\nWith multiple lines."

        )

        label.set_justify(Gtk.Justification.RIGHT)

        vbox_left.pack_start(label, True, True, 0)


        label = Gtk.Label(

            label="This is an example of a line-wrapped label.  It "

            "should not be taking up the entire             "

            "width allocated to it, but automatically "

            "wraps the words to fit.\n"

            "     It supports multiple paragraphs correctly, "

            "and  correctly   adds "

            "many          extra  spaces. "

        )

        label.set_line_wrap(True)

        label.set_max_width_chars(32)

        vbox_right.pack_start(label, True, True, 0)


        label = Gtk.Label(

            label="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

        )

        label.set_line_wrap(True)

        label.set_justify(Gtk.Justification.FILL)

        label.set_max_width_chars(32)

        vbox_right.pack_start(label, True, True, 0)


        label = Gtk.Label()

        label.set_markup(

            "Text can be <small>small</small>, <big>big</big>, "

            "<b>bold</b>, <i>italic</i> and even point to "

            'somewhere in the <a href="https://www.gtk.org" '

            'title="Click to find out more">internets</a>.'

        )

        label.set_line_wrap(True)

        label.set_max_width_chars(48)

        vbox_left.pack_start(label, True, True, 0)


        label = Gtk.Label.new_with_mnemonic(

            "_Press Alt + P to select button to the right"

        )

        vbox_left.pack_start(label, True, True, 0)

        label.set_selectable(True)


        button = Gtk.Button(label="Click at your own risk")

        label.set_mnemonic_widget(button)

        vbox_right.pack_start(button, True, True, 0)


        self.add(hbox)



window = LabelWindow()

window.connect("destroy", Gtk.main_quit)

window.show_all()

Gtk.main()
