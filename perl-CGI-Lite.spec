%define real_name CGI-Lite

Summary:	CGI-Lite module for perl 
Name:		perl-%{real_name}
Version:	2.02
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module can be used to decode form and query information, including file
uploads, as well as cookies in a very simple manner; you need not concern
yourself with the actual details behind the decoding process.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO
%{perl_vendorlib}/CGI/Lite.pm
%{_mandir}/*/*




