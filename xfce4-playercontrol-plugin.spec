
Summary:	Audio player control plugin for the Xfce panel
Name:		xfce4-playercontrol-plugin
Version:	0.3.0
Release:	5
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xmms-plugin
Source0:	http://www.bilimfeneri.gen.tr/ilgar/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libmpd-devel
BuildRequires:	audacious-devel
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
Requires:	xfce4-panel >= 4.4.2

%description
An Audacious and MPD control panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x \
	--enable-audacious \
	--disable-xmms
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%dir %{_datadir}/xfce4/%{name}
%{_datadir}/xfce4/%{name}/*


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-3mdv2010.1
+ Revision: 543434
- rebuild for mdv 2010.1

* Wed Jul 29 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-2mdv2010.0
+ Revision: 404171
- rebuild

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2009.1
+ Revision: 360343
- fix build
- adapt spec file to new plugin name
- xmms plugin is dead

* Fri Nov 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-1mdv2009.1
+ Revision: 305527
- update to new version 0.5.2
- fix url for source

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-8mdv2009.1
+ Revision: 295037
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-7mdv2009.0
+ Revision: 262418
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-6mdv2009.0
+ Revision: 257036
- rebuild

* Sun Jan 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-4mdv2008.1
+ Revision: 158495
- add missing header, patch 0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-3mdv2008.1
+ Revision: 110147
- correct buildrequires
- do not package COPYING and INSTALL files
- use upstream tarball name as a real name
- use upstream name
- spec file clean

  + Thierry Vignaud <tv@mandriva.org>
    - kill changelog left by repsys

  + Jérôme Soyer <saispo@mandriva.org>
    - oops
    - First Build

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-2mdv2008.0
+ Revision: 30434
- update url
- spec file clean
- bump release tag
- new version

