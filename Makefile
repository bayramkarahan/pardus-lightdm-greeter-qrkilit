build:
	: run make install
install:
	mkdir -p $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/module
	cp -prfv module/* $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/module/
	cp -prfv qrkilit.css $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/qrkilit.css
	mkdir -p $(DESTDIR)/usr/share/polkit-1/actions
	mkdir -p $(DESTDIR)/usr/share/polkit-1/rules.d
	cp -prfv qrkilit.policy $(DESTDIR)/usr/share/polkit-1/actions/qrkilit.policy
	cp -prfv qrkilit.rules $(DESTDIR)/usr/share/polkit-1/rules.d/qrkilit.rules
	mkdir -p $(DESTDIR)/usr/bin
	cp -prfv main.py $(DESTDIR)/usr/bin/qrkilit
	
	mkdir -p $(DESTDIR)/usr/share/icons
	cp -prfv qrkilit.svg $(DESTDIR)/usr/share/icons/qrkilit.svg
	
	mkdir -p $(DESTDIR)/usr/share/applications
	cp -prfv qrkilit.desktop $(DESTDIR)/usr/share/applications/qrkilit.desktop

