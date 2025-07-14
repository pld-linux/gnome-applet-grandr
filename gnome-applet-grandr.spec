Summary:	Frontend to the xrandr extension
Summary(pl.UTF-8):	Graficzny interfejs do rozszerzenia xrandr
Name:		gnome-applet-grandr
Version:	0.4.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://kdekorte.googlepages.com/grandr_applet-%{version}.tar.gz
# Source0-md5:	e5503535fad10b1f6e97ed1c1af18960
Patch0:		%{name}-link.patch
Patch1:		%{name}-libpath.patch
URL:		http://kdekorte.googlepages.com/grandr_applet
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-panel-devel >= 2.3.4.1-2
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet is a simple gnome-panel frontend to the xrandr extension
found in XFree86 4.3+ releases.

%description -l pl.UTF-8
Ten aplet jest prostą nakładką dla rozszerzenia xrandr działającą na
panelu GNOME i pozwalającą na zmianę rozdzielczości.

%prep
%setup -q -n grandr_applet-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang grandr_applet

%clean
rm -rf $RPM_BUILD_ROOT

%files -f grandr_applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr (755,root,root) %{_libdir}/grandr
%{_libdir}/bonobo/servers/GrandrApplet.server
%{_pixmapsdir}/grandr.png
