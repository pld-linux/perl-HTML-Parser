%include	/usr/lib/rpm/macros.perl
Summary:	Perl HTML-Parser module
Summary(pl):	Modu³ Perla HTML-Parser
Name:		perl-HTML-Parser
Version:	3.15
Release:	3
LIcense:	Distributable
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.cpan.org/pub/perl/CPAN/modules/by-module/HTML//HTML-Parser-%{version}.tar.gz
Patch0: perl-HTML-Parser-rpmperl-automation-workaround.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tagset
BuildConflicts:	perl-HTML-Stream = 1.45-3
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl HTML-Parser module.

%description -l pl
Modu³ perla pozwalaj±cy analizowaæ pliki HTML.

%prep
%setup -q -n HTML-Parser-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/HTML/*.pm
%dir %{perl_sitearch}/auto/HTML/Parser
%{perl_sitearch}/auto/HTML/Parser/Parser.bs
%attr(755,root,root) %{perl_sitearch}/auto/HTML/Parser/Parser.so
%{_mandir}/man3/*
