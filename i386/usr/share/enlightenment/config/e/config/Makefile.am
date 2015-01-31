MAINTAINERCLEANFILES = Makefile.in
SUBDIRS = tizen

EET_EET = @eet_eet@

EXTRA_DIST = profile.src

filesdir = $(prefix)/config/e/config/

files_DATA = profile.cfg

SUFFIXES = .cfg

.src.cfg:
	$(EET_EET) -i \
	$(top_builddir)/i386/usr/share/enlightenment/config/e/config/$@ config \
	$< 0

clean-local:
	rm -rf *.cfg *~
