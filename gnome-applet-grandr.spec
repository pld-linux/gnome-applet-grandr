Summary:	Frontend to the xrandr extension
Summary(pl):	Nak�adka na rozszerzenie xrandr
Name:		gnome-applet-grandr
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://handhelds.org/~mallum/downloadables/grandr_applet-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel >= 4.2.99
BuildRequires:	gnome-panel-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel
Requires:	XFree86 >= 4.2.99
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet is a simple gnome-panel frontend to the xrandr extension
found in XFree86 4.3+ releases.

%description -l pl
Ten aplet jest prost� nak�adk� dla rozszerzenia xrandr dzia�aj�c� na
panelu gnome i pozwalaj�c� na zmian� rozdzielczo�ci.

%prep
%setup -q -n grandr_applet-%{version}

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
