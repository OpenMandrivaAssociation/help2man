Name:           help2man
Version:        1.38.1
Release:        %mkrel 2
Summary:        Create simple man pages from --help output
Group:          Development/Other
License:        GPLv3
URL:            http://www.gnu.org/software/help2man/
Source0:        ftp://ftp.gnu.org/gnu/help2man/%{name}-%{version}.tar.gz
Requires(post): info-install
Requires(preun): info-install
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
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
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-, root, root)
%doc debian/changelog COPYING INSTALL README NEWS THANKS
%{_bindir}/%{name}
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}.1*
