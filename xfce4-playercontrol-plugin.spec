
Summary:	Audio player control plugin for the Xfce panel
Name:		xfce4-playercontrol-plugin
Version:	0.3.0
Release:	%mkrel 1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xmms-plugin
Source0:	http://www.bilimfeneri.gen.tr/ilgar/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
#BuildRequires:	libmpd-devel
BuildRequires:	audacious-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-xmms-plugin
Obsoletes:	xfce4-xmms-plugin
Provides:	xfce4-xmms-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
An XMMS, Audacious and MPD control panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x \
	--disable-mpd \
	--enable-audacious \
	--disable-xmms
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.*a

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%dir %{_datadir}/xfce4/%{name}
%{_datadir}/xfce4/%{name}/*
