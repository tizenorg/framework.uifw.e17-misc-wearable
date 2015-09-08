MAINTAINERCLEANFILES = Makefile.in

EET_EET = @eet_eet@

EXTRA_DIST = \
         module.comp-tizen.src \
         e.src \
         module.illume2-tizen.src \
         module.devicemgr-tizen.src \
         module.move-tizen.src \
         exehist.src

filesdir = $(prefix)/config/e/config/tizen/
files_DATA = \
             module.comp-tizen.cfg \
             e.cfg \
             module.illume2-tizen.cfg \
             module.devicemgr-tizen.cfg \
             module.move-tizen.cfg \
             exehist.cfg

SUFFIXES = .cfg

.src.cfg:
	$(EET_EET) -e \
	$(top_builddir)/arm/usr/share/enlightenment/config/e/config/tizen/$@ config \
	$< 1

clean-local:
	rm -rf *.cfg *~
