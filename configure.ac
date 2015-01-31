
AC_INIT(e17-misc-wearable, 1.0, doyoun.kang@samsung.com)
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR(configure.ac)

AC_PREFIX_DEFAULT(/usr/share/enlightenment)

PKG_CHECK_MODULES(E_MISC, [eet edje])
AC_ARG_WITH(edje-cc,
[  --with-edje-cc=PATH              specify a specific path to edje_cc],
[
   v=$withval;
   edje_cc=$v
   echo "  Enlightenment edje_cc explicitly set to "$edje_cc;
],[
   edje_cc=$(pkg-config --variable=prefix edje)/bin/edje_cc
])
AC_SUBST(edje_cc)

AC_ARG_WITH(eet-eet,
[   --with-eet-eet=PATH             specify a specific path to eet utility],
[
   v=$withval;
   eet_eet=$v
   echo "   Enlightenment eet explicitly set to "$eet_eet;
],[
   eet_eet=$(pkg-config --variable=prefix eet)/bin/eet
])
AC_SUBST(eet_eet)

AC_CONFIG_FILES([
Makefile
arm/Makefile
arm/usr/Makefile
arm/usr/share/Makefile
arm/usr/share/enlightenment/Makefile
arm/usr/share/enlightenment/config/Makefile
arm/usr/share/enlightenment/config/e/Makefile
arm/usr/share/enlightenment/config/e/config/Makefile
arm/usr/share/enlightenment/config/e/config/tizen/Makefile
arm/usr/share/enlightenment/data/Makefile
arm/usr/share/enlightenment/data/themes/Makefile
arm/usr/share/enlightenment/data/themes/images/Makefile
i386/Makefile
i386/usr/Makefile
i386/usr/share/Makefile
i386/usr/share/enlightenment/Makefile
i386/usr/share/enlightenment/config/Makefile
i386/usr/share/enlightenment/config/e/Makefile
i386/usr/share/enlightenment/config/e/config/Makefile
i386/usr/share/enlightenment/config/e/config/tizen/Makefile
i386/usr/share/enlightenment/data/Makefile
i386/usr/share/enlightenment/data/themes/Makefile
i386/usr/share/enlightenment/data/themes/images/Makefile
])
AC_OUTPUT
