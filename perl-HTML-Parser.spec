%include	/usr/lib/rpm/macros.perl
Summary:	Perl HTML-Parser module
Summary(pl):	Modu³ Perla HTML-Parser
Name:		perl-HTML-Parser
Version:	3.05
Release:	2
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML-Parser-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-libwww
BuildConflicts:	perl-HTML-Stream = 1.45-3
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Perl HTML-Parser module.

%description -l pl
Modu³ perla pozwalaj±cy analizowaæ pliki HTML.

%prep
%setup -q -n HTML-Parser-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/HTML/Parser/*.so

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
%{perl_sitearch}/HTML/*.pm

%dir %{perl_sitearch}/auto/HTML/Parser
%{perl_sitearch}/auto/HTML/Parser/.packlist
%{perl_sitearch}/auto/HTML/Parser/Parser.bs
%attr(755,root,root) %{perl_sitearch}/auto/HTML/Parser/Parser.so

%{_mandir}/man3/*
