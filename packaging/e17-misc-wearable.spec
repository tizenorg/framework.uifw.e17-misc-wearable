Name:       e17-misc-wearable
Summary:    E17 Config files for wearable
Version:    0.13.1
Release:    1
Group:      System/GUI/Other
License:    BSD
Source0:    %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(eet)
BuildRequires: pkgconfig(edje)
BuildRequires: eet-bin
BuildRequires: edje-bin
Requires:   e17

%description
The E17 extra configuration files for wearable

%prep
%setup -q

%build

%autogen
%configure --prefix=/usr/share/enlightenment
make

%install
rm -rf %{buildroot}

# for license notification
mkdir -p %{buildroot}/usr/share/license
cp -a COPYING %{buildroot}/usr/share/license/%{name}

# Please do not remove the following 1 line
%__mkdir_p %{buildroot}/opt/home/app/.e

%__mkdir_p %{buildroot}/etc/X11
%__cp -afr scripts/wmrc %{buildroot}/etc/X11/wmrc

%__mkdir_p %{buildroot}/usr/share/enlightenment/config/apps
%__cp -afr %{_arch}/usr/share/enlightenment/config/apps/* %{buildroot}/usr/share/enlightenment/config/apps

%__mkdir_p %{buildroot}/usr/share/enlightenment/config/e/applications
%__cp -afr %{_arch}/usr/share/enlightenment/config/e/applications/* %{buildroot}/usr/share/enlightenment/config/e/applications

%__mkdir_p %{buildroot}/usr/share/enlightenment/config/e/backgrounds
%__cp -afr %{_arch}/usr/share/enlightenment/config/e/backgrounds/* %{buildroot}/usr/share/enlightenment/config/e/backgrounds

%__mkdir_p %{buildroot}/usr/share/enlightenment/config/e/config
%__cp -afr %{_arch}/usr/share/enlightenment/config/e/config/*.cfg %{buildroot}/usr/share/enlightenment/config/e/config/

%__mkdir_p %{buildroot}/usr/share/enlightenment/config/e/config/tizen
%__cp -afr %{_arch}/usr/share/enlightenment/config/e/config/tizen/*.cfg %{buildroot}/usr/share/enlightenment/config/e/config/tizen/

%__mkdir_p %{buildroot}/usr/share/enlightenment/data/themes
%__cp -afr %{_arch}/usr/share/enlightenment/data/themes/*.edj %{buildroot}/usr/share/enlightenment/data/themes

%__mkdir_p %{buildroot}/usr/share/enlightenment/data/images
%__cp -afr %{_arch}/usr/share/enlightenment/data/images/* %{buildroot}/usr/share/enlightenment/data/images

%pre
if [ ! -e "/usr/share/enlightenment/config" ]
then
	mkdir -p /usr/share/enlightenment/config
fi
chmod 755 /usr/share/enlightenment/config

%post
chmod 644 /usr/share/enlightenment/config/e/config/*.cfg
chmod 644 /usr/share/enlightenment/config/e/config/tizen/*.cfg
#chmod 644 /usr/share/enlightenment/data/themes/*.edj
chown -R app.app /opt/home/app/.e

%files
%manifest e17-misc-wearable.manifest
%defattr(-,root,root,-)
/opt/home/app/.e
/etc/X11/wmrc
%exclude /usr/share/enlightenment/data/themes/*
/usr/share/enlightenment/data/images/*
/usr/share/enlightenment/config
/usr/share/enlightenment/config/apps/*
/usr/share/enlightenment/config/e/applications/*
%exclude /usr/share/enlightenment/config/e/backgrounds/*
/usr/share/enlightenment/config/e/config/*.cfg
/usr/share/enlightenment/config/e/config/tizen/*.cfg
/usr/share/license/%{name}
%exclude /usr/share/enlightenment/config/apps/*
