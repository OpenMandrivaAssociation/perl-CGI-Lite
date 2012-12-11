%define upstream_name    CGI-Lite
%define upstream_version 2.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	CGI-Lite module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module can be used to decode form and query information, including file
uploads, as well as cookies in a very simple manner; you need not concern
yourself with the actual details behind the decoding process.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc CHANGES README TODO
%{perl_vendorlib}/CGI/Lite.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.20.0-2mdv2011.0
+ Revision: 680690
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.20.0-1mdv2011.0
+ Revision: 406868
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.02-5mdv2009.0
+ Revision: 255774
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-3mdv2008.1
+ Revision: 136905
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.02-2mdv2007.0
+ Revision: 73387
- import perl-CGI-Lite-2.02-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.02-2mdk
- Fix SPEC Using perl Policies
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.02-1mdk
- initial Mandriva package

