Summary:	Frontend to the xrandr extension
Summary(pl.UTF-8):	Nakładka na rozszerzenie xrandr
Name:		gnome-applet-grandr
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dekorte.homeip.net/download/grandr-applet/grandr_applet-%{version}.tar.gz
# Source0-md5:	e5503535fad10b1f6e97ed1c1af18960
URL:		http://dekorte.homeip.net/download/grandr-applet/
Patch0:		%{name}-libXext.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.3.4.1-2
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	pkgconfig
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
