%include	/usr/lib/rpm/macros.perl
%define		__find_requires %{_builddir}/HTML-Parser-%{version}/find-perl-requires
Summary:	Perl HTML-Parser module
Summary(pl):	Modu³ Perla HTML-Parser
Name:		perl-HTML-Parser
Version:	2.23
Release:	4
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML-Parser-%{version}.tar.gz
Patch:		perl-HTML-Parser-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Perl HTML-Parser module.

%description -l pl
Modu³ perla pozwalaj±cy analizowaæ pliki HTML.

%prep
%setup -q -n HTML-Parser-%{version}
%patch -p1

chmod +x find-perl-requires

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/Parser/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/HTML/*.pm

%{perl_sitearch}/auto/HTML/Parser

%{_mandir}/man3/*
