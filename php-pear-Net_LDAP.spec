%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       LDAP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - OO interface for searching and manipulating LDAP-entries
Summary(pl):	%{_pearname} - zorientowany obiektowo interfejs do szukania i manipulowania pozycjami LDAP
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	47b79f60968d3737188838d72a0dfd4c
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

This class has in PEAR status: %{_status}.

%description -l pl
%{_pearname} jest klonem Perlowego Net::LDAP, obiektowego interfejsu do
serwerów ldap. Nie posiada wszystkich mo¿liwo¶ci Net::LDAP, (obs³uga
ldif, schematy, itp), ale ma nastêpuj±ce cechy:
- prosty interfejs obiektowy do po³±czeñ, wyszukiwañ i dodawania nowych
  pozycji
- wsparcie dla TLS i ldap v3
- mo¿liwo¶æ prostych modyfikacji, usuwania i tworzenia ldapentries

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{doc,tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
