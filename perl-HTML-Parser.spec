%include	/usr/lib/rpm/macros.perl
Summary:	Perl HTML::Parser module
Summary(pl):	Modu³ Perla HTML::Parser
Name:		perl-HTML-Parser
Version:	3.25
Release:	3
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/HTML//HTML-Parser-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tagset
BuildConflicts:	perl-HTML-Stream = 1.45-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# HTTP::Headers (perl-libwww) is not always required
%define		_noautoreq	"perl(HTTP::Headers)"

%description
Perl HTML::Parser module.

%description -l pl
Modu³ perla pozwalaj±cy analizowaæ pliki HTML.

%prep
%setup -q -n HTML-Parser-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitearch}/HTML
%{perl_sitearch}/HTML/*.pm
%dir %{perl_sitearch}/auto/HTML
%dir %{perl_sitearch}/auto/HTML/Parser
%{perl_sitearch}/auto/HTML/Parser/Parser.bs
%attr(755,root,root) %{perl_sitearch}/auto/HTML/Parser/Parser.so
%{_mandir}/man3/*
