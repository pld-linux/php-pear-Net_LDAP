%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	LDAP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - OO interface for searching and manipulating LDAP-entries
Summary(pl):	%{_pearname} - obiektowy interfejs do przeszukiwania i modyfikowania wpisów LDAP
Name:		php-pear-%{_pearname}
Version:	0.6.6
Release:	4
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d19f11c671122d0ff30928d86a868096
Patch0:		%{name}-path_fix.patch
Patch1:		%{name}-bug-8286.patch
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

%description -l pl
%{_pearname} jest klonem perlowego Net::LDAP, czyli zorientowanego
obiektowo interfejsu do serwerów LDAP. Nie posiada wszystkich
mo¿liwo¶ci Net::LDAP (obs³uga ldif, schematy, itp), ale ma nastêpuj±ce
cechy:
- prosty interfejs obiektowy do po³±czeñ, wyszukiwañ i dodawania
  nowych pozycji
- obs³uga TLS i LDAP v3
- mo¿liwo¶æ prostych modyfikacji, usuwania i tworzenia wpisów LDAP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

rm -f docs/%{_pearname}/LICENSE # GPL V2.1

install -d ./%{php_pear_dir}/tests/%{_pearname}
mv docs/%{_pearname}/tests/* ./%{php_pear_dir}/tests/%{_pearname}
rmdir docs/%{_pearname}/tests

%patch1 -p1
cd ./%{php_pear_dir}/%{_class}
%patch0 -p2

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
