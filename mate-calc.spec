%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE desktop calculator
Name:		mate-calc
Version:	1.18.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
#Patch0:	mate-calc-1.4.0-rosa-yyscan_t.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	yelp-tools

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a desktop calculator. It has Basic, Financial and
Scientific modes. Internally it uses multiple precision arithmetic to
produce results to a high degree of accuracy.

%files -f %{name}.lang
%doc README NEWS AUTHORS 
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	 --disable-schemas-compile \
	 %{nil}
%make

%install
%makeinstall_std

# .desktop
desktop-file-edit \
	--remove-category=MATE \
	--add-category=X-MATE \
	%{buildroot}%{_datadir}/applications/mate-calc.desktop

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

