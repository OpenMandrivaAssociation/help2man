Summary:	Create simple man pages from --help output
Name:		help2man
Version:	1.47.17
Release:	1
Group:		Development/Other
License:	GPLv3
Url:		http://www.gnu.org/software/help2man/
Source0:	ftp://ftp.gnu.org:21/gnu/help2man/%{name}-%{version}.tar.xz
BuildRequires:	perl-Locale-gettext

%description
help2man is a script to create simple man pages from the --help and 
--version output of programs.

Since most GNU documentation is now in info format, this provides a way 
to generate a placeholder man page pointing to that resource while still 
providing some useful information.

%prep
%autosetup -p1

%build
%configure --enable-nls
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc debian/changelog COPYING INSTALL README NEWS THANKS
%{_bindir}/%{name}
%{_libdir}/%{name}/bindtextdomain.so
%{_infodir}/%{name}*.info*
%{_mandir}/man1/%{name}.1*
%{_mandir}/*/man1/%{name}.1*
