Summary:	Create simple man pages from --help output
Name:		help2man
Version:	1.49.3
Release:	2
Group:		Development/Other
License:	GPLv3
Url:		https://www.gnu.org/software/help2man/
Source0:	https://ftp.gnu.org/gnu/help2man/%{name}-%{version}.tar.xz
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
%doc %{_infodir}/%{name}*.info*
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/*/man1/%{name}.1*
