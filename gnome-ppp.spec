%define name gnome-ppp
%define version 0.3.23
%define release %mkrel 4
%define section Internet/Remote Access

Summary: Gnome 2 front-end to wvdial
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://www.gnome-ppp.org/download/0.3/%{name}-%{version}.tar.bz2
Source1: gnome-ppp.png
Source2: gnome-ppp-16.png
Source3: gnome-ppp-32.png
URL: http://www.gnome-ppp.org/
License: GPL
Group: System/Configuration/Networking
Requires: wvdial >= 1.54
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gnome 2 front-end to wvDial, a modem/ISDN dial-up software.
%prep
%setup -q 

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir %{buildroot}/%{_datadir}/pixmaps && \
cp -r %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/ %{buildroot}/%{_datadir}/pixmaps/
#mv %{buildroot}/%{_datadir}/doc/%{name}-%{version} %{buildroot}/%{_datadir}/doc/%{name}
rm -rf %{buildroot}/%{_datadir}/doc/%{name}

%find_lang %{name} --with-gnome

# menu

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="GNOME" \
	--add-category="Settings;Network" \
	--add-category="X-MandrivaLinux-System-Configuration-Networking" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
#install -m 644 src/pixmaps/%name.png %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)

%doc ChangeLog COPYING INSTALL

%{_bindir}/gnome-ppp
%{_datadir}/applications/gnome-ppp.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade/*
%{_datadir}/pixmaps/apps/%name.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/%name/gnome_ppp*.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png



