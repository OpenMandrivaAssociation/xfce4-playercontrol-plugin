Summary:	XMMS control plugin for the Xfce panel
Name:		xfce4-xmms-plugin
Version:	0.5.2
Release:	%mkrel 1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xmms-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-xmms-plugin/%{name}-%{version}.tar.bz2
Patch0:		xfce4-xmms-plugin-0.5.1.patch
Requires:	xfce4-panel >= 4.4.2
Requires:	xmms
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	xmms-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	glib2-devel
BuildRequires:	gtk+-devel
Obsoletes:	xfce-xmms-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
An XMMS control panel plugin for the Xfce Desktop Environment.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
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
%dir %{_datadir}/xfce4/xfce4-xmms-plugin
%{_datadir}/xfce4/xfce4-xmms-plugin/*
