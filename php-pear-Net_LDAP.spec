%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	LDAP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - OO interface for searching and manipulating LDAP-entries
Summary(pl.UTF-8):	%{_pearname} - obiektowy interfejs do przeszukiwania i modyfikowania wpisów LDAP
Name:		php-pear-%{_pearname}
Version:	1.1.4
Release:	1
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	044877f80abc6292808708c3951f80a9
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/Net_LDAP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} is a clone of Perl's Net::LDAP object interface to
ldapservers. It does not contain all of Net::LDAP features (ldif
handling, schemas, etc), but has:
- a simple OO interface to connections, searches and entries
- support for TLS and ldap v3
- simple modification, deletion and creation of ldapentries

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
%{_pearname} jest klonem perlowego Net::LDAP, czyli zorientowanego
obiektowo interfejsu do serwerów LDAP. Nie posiada wszystkich
możliwości Net::LDAP (obsługa ldif, schematy, itp), ale ma następujące
cechy:
- prosty interfejs obiektowy do połączeń, wyszukiwań i dodawania
  nowych pozycji
- obsługa TLS i LDAP v3
- możliwość prostych modyfikacji, usuwania i tworzenia wpisów LDAP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

cd ./%{php_pear_dir}/%{_class}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
