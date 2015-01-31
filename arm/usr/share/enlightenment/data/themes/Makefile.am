MAINTAINERCLEANFILES = Makefile.in
SUBDIRS = images

EDJE_CC = @edje_cc@
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
EDJE_FLAGS = $(EDJE_FLAGS_$(V)) \
-id $(top_srcdir)/arm/usr/share/enlightenment/data/themes/images \
-fd $(top_srcdir)/arm/usr/share/enlightenment/data/themes/fonts

filesdir = $(datadir)/enlightenment/data/themes
files_DATA = \
tizen.edj

EXTRA_DIST = \
tizen.edc

tizen.edj: Makefile $(EXTRA_DIST)
	$(EDJE_CC) $(EDJE_FLAGS) \
	$(top_srcdir)/arm/usr/share/enlightenment/data/themes/tizen.edc \
	$(top_builddir)/arm/usr/share/enlightenment/data/themes/tizen.edj

clean-local:
	rm -f *.edj
