Name:           perl-TimeDate
Version:        1.20
Release: 	1
Summary:        A Perl module for time and date manipulation

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/TimeDate/
Source0:   http://www.cpan.org/authors/id/G/GB/GBARR/TimeDate-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl

%description
This module includes a number of smaller modules suited for
manipulation of time and date strings with Perl.  In particular, the
Date::Format and Date::Parse modules can display and read times and
dates in various formats, providing a more reliable interface to
textual representations of points in time.


%prep
%setup -q -n TimeDate-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%{perl_vendorlib}/Date/*
%{perl_vendorlib}/Time/*
%doc %{_mandir}/man3/*.3*


