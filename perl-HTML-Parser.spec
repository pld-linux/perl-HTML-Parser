%include	/usr/lib/rpm/macros.perl
Summary:	Perl HTML::Parser module
Summary(pl):	ModuЁ Perla HTML::Parser
Summary(pt_BR):	MСdulo Perl HTML::Parser
Summary(ru): HTML::Parser - набор модулей для "разбора" HTML-документов.
Summary(uk): HTML::Parser - наб╕р модул╕в для розбору HTML-документ╕в
Name:		perl-HTML-Parser
Version:	3.26
Release:	12
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/HTML//HTML-Parser-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tagset
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildConflicts:	perl-HTML-Stream = 1.45-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# HTTP::Headers (perl-libwww) is not always required
%define		_noautoreq	"perl(HTTP::Headers)"

%description
Perl module HTML::Parser that alloe parse and extract information from
HTML documents.

%description -l pl
ModuЁ Perla HTML::Parser pozwalaj╠cy na parsowanie i wyciaganie
informacji z dokumentu HTML.

%description -l pt_BR
MСdulo Perl HTML::Parser - Uma coleГЦo de mСdulos para examinar e
extrair informaГУes de documentos HTML.

%description -l ru
HTML::Parser - набор модулей для "разбора" HTML-документов.

%description -l uk
HTML::Parser - наб╕р модул╕в для розбору HTML-документ╕в.

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
