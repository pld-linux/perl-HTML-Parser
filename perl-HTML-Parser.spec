#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Parser
Summary:	HTML::Parser - parsing and extracting information from HTML documents
Summary(cs.UTF-8):	HTML::Parser - modul pro parsování HTML v Perlu
Summary(pl.UTF-8):	HTML::Parser - analiza i wyciąganie informacji z dokumentów HTML
Summary(ru.UTF-8):	HTML::Parser - набор модулей для "разбора" HTML-документов
Summary(uk.UTF-8):	HTML::Parser - набір модулів для розбору HTML-документів
Summary(zh_CN.UTF-8):	Perl 的 HTML 解析器模块。
Name:		perl-HTML-Parser
Version:	3.59
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	190950f442ff4a8e59e637714105a01b
URL:		http://search.cpan.org/dist/HTML-Parser/
BuildRequires:	perl-HTML-Tagset >= 3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildConflicts:	perl-HTML-Stream = 1.45-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# HTTP::Headers (perl-libwww) is not always required
%define		_noautoreq	'perl(HTTP::Headers)'

%description
Perl module HTML::Parser that allows to parse and extract information
from HTML documents.

%description -l cs.UTF-8
Balíček perl-HTML-Parser obsahuje modul pro Perl, který slouží k
parsování a extrahování informací z HTML dokumentu.

%description -l da.UTF-8
HTML::Parser modul til Perl for at tolka og extrahere information fra
HTML-dokument.

%description -l de.UTF-8
HTML::Parser modul für Perl zum Parsen und Extrahieren von
Informationen aus HTML-Dokumenten.

%description -l es.UTF-8
Módulo HTML::Parser para perl para analizar y extraer información a
partir de documentos HTML.

%description -l fr.UTF-8
Module HTML::Parser pour perl permettant d'analyser et d'extraire des
informations de documents HTML.

%description -l it.UTF-8
Il modulo HTML::Parser per perl, che consente di analizzare documenti
HTML e di estrarne informazioni.

%description -l ja.UTF-8
HTML ドキュメントから情報を解析、抽出するための Perl 用の HTML::Parser
。

%description -l ko.UTF-8
HTML::Parser 모줄은 펄이 HTML 문서들로 부터 정보를 파싱하고 가져오게끔
합니다.

%description -l pl.UTF-8
Moduł Perla HTML::Parser pozwalający na parsowanie i wyciąganie
informacji z dokumentu HTML.

%description -l pt_BR.UTF-8
Módulo Perl HTML::Parser - Uma coleção de módulos para examinar e
extrair informações de documentos HTML.

%description -l ru.UTF-8
HTML::Parser - набор модулей для "разбора" HTML-документов.

%description -l uk.UTF-8
HTML::Parser - набір модулів для розбору HTML-документів.

%description -l pt.UTF-8
O módulo HTML::Parser para o Perl analisar e extrair informações de
documentos HTML.

%description -l sv.UTF-8
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
	CC="%{__cc}" \
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
%doc Changes README TODO
%dir %{perl_vendorarch}/HTML
%{perl_vendorarch}/HTML/*.pm
%dir %{perl_vendorarch}/auto/HTML
%dir %{perl_vendorarch}/auto/HTML/Parser
%{perl_vendorarch}/auto/HTML/Parser/Parser.bs
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Parser/Parser.so
%{_mandir}/man3/*
