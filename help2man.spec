Name:           help2man
Version:        1.40.2
Release:        3
Summary:        Create simple man pages from --help output
Group:          Development/Other
License:        GPLv3
URL:            http://www.gnu.org/software/help2man/
Source0:        ftp://ftp.gnu.org/gnu/help2man/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
help2man is a script to create simple man pages from the --help and 
--version output of programs.

Since most GNU documentation is now in info format, this provides a way 
to generate a placeholder man page pointing to that resource while still 
providing some useful information.

%prep
%setup -q

%build
%configure --disable-nls
%make

%install
%makeinstall

%files
%defattr(-, root, root)
%doc debian/changelog COPYING INSTALL README NEWS THANKS
%{_bindir}/%{name}
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 1.40.2-1mdv2011.0
+ Revision: 683295
- version 1.40.2
- version 1.40.2

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.38.1-3
+ Revision: 665408
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.38.1-2mdv2011.0
+ Revision: 605853
- rebuild

* Tue Apr 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.38.1-1mdv2010.1
+ Revision: 539434
- New version 1.38.1

* Thu Dec 24 2009 Jérôme Brenier <incubusss@mandriva.org> 1.37.1-1mdv2010.1
+ Revision: 481961
- new version 1.37.1
- use %%configure instead of %%configure2_5x
- fix license tag
- fix Source url
- fix doc list (ChangeLog is only a symlink)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.36.4-7mdv2010.0
+ Revision: 425141
- rebuild

* Tue Dec 30 2008 Oden Eriksson <oeriksson@mandriva.com> 1.36.4-6mdv2009.1
+ Revision: 321321
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.36.4-5mdv2009.0
+ Revision: 221126
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.36.4-4mdv2008.1
+ Revision: 150253
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.36.4-3mdv2008.0
+ Revision: 70271
- kill file require on info-install

* Thu Jul 05 2007 Adam Williamson <awilliamson@mandriva.org> 1.36.4-2mdv2008.0
+ Revision: 48484
- rebuild for 2008
- Import help2man



* Fri Sep 08 2006 David Walluck <walluck@mandriva.org> 1.36.4-1mdv2007.0
- 1.36.4

* Mon Aug 15 2005 David Walluck <walluck@mandriva.org> 1.35.1-1mdk
- release
