%define upstream_name    CGI-Lite
Name:		perl-%{upstream_name}
Version:	3.03
Release:	2

Summary:	CGI-Lite module for perl 


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://gitlab.com/openstrike/cgi-lite
Source0:	https://cpan.metacpan.org/authors/id/H/HO/HOUSTON/CGI-Lite-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module can be used to decode form and query information, including file
uploads, as well as cookies in a very simple manner; you need not concern
yourself with the actual details behind the decoding process.

%prep
%setup -q -n %{upstream_name}-%{version}

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




