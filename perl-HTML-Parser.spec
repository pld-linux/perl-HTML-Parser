%include	/usr/lib/rpm/macros.perl
Summary:	Perl HTML-Parser module
Summary(pl):	Modu� Perla HTML-Parser
Name:		perl-HTML-Parser
Version:	3.05
Release:	4
LIcense:	Distributable
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML-Parser-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libwww
BuildConflicts:	perl-HTML-Stream = 1.45-3
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl HTML-Parser module.

%description -l pl
Modu� perla pozwalaj�cy analizowa� pliki HTML.

%prep
%setup -q -n HTML-Parser-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

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
