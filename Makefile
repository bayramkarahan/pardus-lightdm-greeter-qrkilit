build:
	: run make install
install:
	mkdir -p $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/module
	cp -prfv module/* $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/module/
	cp -prfv qrkilit.css $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/qrkilitkurum.css
	mkdir -p $(DESTDIR)/usr/share/polkit-1/actions
	mkdir -p $(DESTDIR)/usr/share/polkit-1/rules.d
	cp -prfv qrkilit.policy $(DESTDIR)/usr/share/polkit-1/actions/qrkilitkurum.policy
	cp -prfv qrkilit.rules $(DESTDIR)/usr/share/polkit-1/rules.d/qrkilitkurum.rules
	mkdir -p $(DESTDIR)/usr/bin
	cp -prfv main.py $(DESTDIR)/usr/bin/qrkilitkurum
	
	mkdir -p $(DESTDIR)/usr/share/icons
	cp -prfv qrkilit.svg $(DESTDIR)/usr/share/icons/qrkilitkurum.svg
	
	mkdir -p $(DESTDIR)/usr/share/applications
	cp -prfv qrkilit.desktop $(DESTDIR)/usr/share/applications/qrkilitkurum.desktop

