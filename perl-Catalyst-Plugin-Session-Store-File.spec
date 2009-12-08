%define upstream_name    Catalyst-Plugin-Session-Store-File
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	File storage backend for session data
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Nagios/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Cache::Cache) >= 1.02
BuildRequires:	perl(Catalyst) >= 5
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.01
BuildRequires:	perl(Class::Accessor::Fast) >= 0.22
BuildRequires:	perl(Class::Data::Inheritable) >= 0.04

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

Provides:   perl-Catalyst-P-S-Store-File
Obsoletes:  perl-Catalyst-P-S-Store-File

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess cache.
It is based on Cache::FileCache.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*
