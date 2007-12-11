%define realname Catalyst-Plugin-Session-Store-File
%define name	perl-%{realname}
%define version	0.10
%define release	%mkrel 2

Summary:	File storage backend for session data
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:	perl(Cache::Cache) >= 1.02
BuildRequires:	perl(Catalyst) >= 5
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.01
BuildRequires:	perl(Class::Accessor::Fast) >= 0.22
BuildRequires:	perl(Class::Data::Inheritable) >= 0.04
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess cache.
It is based on Cache::FileCache.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

