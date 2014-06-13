Summary:	Create simple man pages from --help output
Name:		help2man
Version:	1.45.1
Release:	2
Group:		Development/Other
License:	GPLv3
Url:		http://www.gnu.org/software/help2man/
Source0:	ftp://ftp.gnu.org/gnu/help2man/%{name}-%{version}.tar.xz
BuildArch:	noarch

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
%doc debian/changelog COPYING INSTALL README NEWS THANKS
%{_bindir}/%{name}
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}.1*

