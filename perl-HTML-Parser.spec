
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Parser
Summary:	Perl HTML::Parser module
Summary(cs):	Modul pro parsování HTML v Perlu
Summary(da):	HTML::Parser modul til Perl
Summary(de):	HTML::Parser Modul für Perl
Summary(es):	Módulo HTML::Parser para Perl
Summary(fr):	Module HTML::Parser pour Perl
Summary(it):	Modulo HTML::Parser per Perl
Summary(ja):	Perl ÍÑ HTML::Parser
Summary(ko):	ÆŞÀ» À§ÇÑ HTML::Parser ¸ğÁÙ
Summary(pl):	Modu³ Perla HTML::Parser
Summary(pt):	O módulo HTML::Parser para o Perl
Summary(pt_BR):	Módulo Perl HTML::Parser
Summary(ru):	HTML::Parser - ÎÁÂÏÒ ÍÏÄÕÌÅÊ ÄÌÑ "ÒÁÚÂÏÒÁ" HTML-ÄÏËÕÍÅÎÔÏ×
Summary(sv):	HTML::Parser-modul till Perl
Summary(uk):	HTML::Parser - ÎÁÂ¦Ò ÍÏÄÕÌ¦× ÄÌÑ ÒÏÚÂÏÒÕ HTML-ÄÏËÕÍÅÎÔ¦×
Summary(zh_CN):	Perl µÄ HTML ½âÎöÆ÷Ä£¿é¡£
Name:		perl-HTML-Parser
Version:	3.33
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	088285128121d4c09da4e2c87953f9f3
BuildRequires:	perl-HTML-Tagset
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildConflicts:	perl-HTML-Stream = 1.45-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# HTTP::Headers (perl-libwww) is not always required
%define		_noautoreq	'perl(HTTP::Headers)'

%description
Perl module HTML::Parser that allows to parse and extract information
from HTML documents.

%description -l cs
Balíèek perl-HTML-Parser obsahuje modul pro Perl, kterı slou¾í k
parsování a extrahování informací z HTML dokumentu.

%description -l da
HTML::Parser modul til Perl for at tolka og extrahere information fra
HTML-dokument.

%description -l de
HTML::Parser modul für Perl zum Parsen und Extrahieren von
Informationen aus HTML-Dokumenten.

%description -l es
Módulo HTML::Parser para perl para analizar y extraer información a
partir de documentos HTML.

%description -l fr
Module HTML::Parser pour perl permettant d'analyser et d'extraire des
informations de documents HTML.

%description -l it
Il modulo HTML::Parser per perl, che consente di analizzare documenti
HTML e di estrarne informazioni.

%description -l ja
HTML ¥É¥­¥å¥á¥ó¥È¤«¤é¾ğÊó¤ò²òÀÏ¡¢Ãê½Ğ¤¹¤ë¤¿¤á¤Î Perl ÍÑ¤Î HTML::Parser
¡£

%description -l ko
HTML::Parser ¸ğÁÙÀº ÆŞÀÌ HTML ¹®¼­µé·Î ºÎÅÍ Á¤º¸¸¦ ÆÄ½ÌÇÏ°í °¡Á®¿À°Ô²û
ÇÕ´Ï´Ù.

%description -l pl
Modu³ Perla HTML::Parser pozwalaj±cy na parsowanie i wyciaganie
informacji z dokumentu HTML.

%description -l pt_BR
Módulo Perl HTML::Parser - Uma coleção de módulos para examinar e
extrair informações de documentos HTML.

%description -l ru
HTML::Parser - ÎÁÂÏÒ ÍÏÄÕÌÅÊ ÄÌÑ "ÒÁÚÂÏÒÁ" HTML-ÄÏËÕÍÅÎÔÏ×.

%description -l uk
HTML::Parser - ÎÁÂ¦Ò ÍÏÄÕÌ¦× ÄÌÑ ÒÏÚÂÏÒÕ HTML-ÄÏËÕÍÅÎÔ¦×.

%description -l pt
O módulo HTML::Parser para o Perl analisar e extrair informações de
documentos HTML.

%description -l sv
HTML::Parser modul till perl för att tolka och extrahera information
från HTML-dokument.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	DEFINE="-DMARKED_SECTION -DUNICODE_ENTITIES" \
	< /dev/null
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/HTML
%{perl_vendorarch}/HTML/*.pm
%dir %{perl_vendorarch}/auto/HTML
%dir %{perl_vendorarch}/auto/HTML/Parser
%{perl_vendorarch}/auto/HTML/Parser/Parser.bs
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Parser/Parser.so
%{_mandir}/man3/*
