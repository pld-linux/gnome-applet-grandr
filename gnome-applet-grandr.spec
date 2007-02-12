Summary:	Frontend to the xrandr extension
Summary(pl.UTF-8):   Nakładka na rozszerzenie xrandr
Name:		gnome-applet-grandr
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://handhelds.org/~mallum/downloadables/grandr_applet-%{version}.tar.gz
# Source0-md5:	873e08f69d6e2c4d9d433895f3a5dfd4
Patch0:		%{name}-libXext.patch
BuildRequires:	XFree86-devel >= 4.2.99
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.3.4.1-2
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	pkgconfig
Requires:	XFree86 >= 4.2.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet is a simple gnome-panel frontend to the xrandr extension
found in XFree86 4.3+ releases.

%description -l pl.UTF-8
Ten aplet jest prostą nakładką dla rozszerzenia xrandr działającą na
panelu GNOME i pozwalającą na zmianę rozdzielczości.

%prep
%setup -q -n grandr_applet-%{version}
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr (755,root,root) %{_libdir}/grandr
%{_libdir}/bonobo/servers/*
%{_pixmapsdir}/*
