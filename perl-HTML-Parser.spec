#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Parser
Summary:	HTML::Parser - parsing and extracting information from HTML documents
Summary(cs):	HTML::Parser - modul pro parsov�n� HTML v Perlu
Summary(pl):	HTML::Parser - analiza i wyci�ganie informacji z dokument�w HTML
Summary(ru):	HTML::Parser - ����� ������� ��� "�������" HTML-����������
Summary(uk):	HTML::Parser - ��¦� ����̦� ��� ������� HTML-�������Ԧ�
Summary(zh_CN):	Perl �� HTML ������ģ�顣
Name:		perl-HTML-Parser
Version:	3.37
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c7705c9db7da429cfd2d72ab3ebb22f1
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

%description -l cs
Bal��ek perl-HTML-Parser obsahuje modul pro Perl, kter� slou�� k
parsov�n� a extrahov�n� informac� z HTML dokumentu.

%description -l da
HTML::Parser modul til Perl for at tolka og extrahere information fra
HTML-dokument.

%description -l de
HTML::Parser modul f�r Perl zum Parsen und Extrahieren von
Informationen aus HTML-Dokumenten.

%description -l es
M�dulo HTML::Parser para perl para analizar y extraer informaci�n a
partir de documentos HTML.

%description -l fr
Module HTML::Parser pour perl permettant d'analyser et d'extraire des
informations de documents HTML.

%description -l it
Il modulo HTML::Parser per perl, che consente di analizzare documenti
HTML e di estrarne informazioni.

%description -l ja
HTML �ɥ�����Ȥ���������ϡ���Ф��뤿��� Perl �Ѥ� HTML::Parser
��

%description -l ko
HTML::Parser ������ ���� HTML ������� ���� ������ �Ľ��ϰ� �������Բ�
�մϴ�.

%description -l pl
Modu� Perla HTML::Parser pozwalaj�cy na parsowanie i wyci�ganie
informacji z dokumentu HTML.

%description -l pt_BR
M�dulo Perl HTML::Parser - Uma cole��o de m�dulos para examinar e
extrair informa��es de documentos HTML.

%description -l ru
HTML::Parser - ����� ������� ��� "�������" HTML-����������.

%description -l uk
HTML::Parser - ��¦� ����̦� ��� ������� HTML-�������Ԧ�.

%description -l pt
O m�dulo HTML::Parser para o Perl analisar e extrair informa��es de
documentos HTML.

%description -l sv
HTML::Parser modul till perl f�r att tolka och extrahera information
fr�n HTML-dokument.

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
%doc Changes README TODO
%dir %{perl_vendorarch}/HTML
%{perl_vendorarch}/HTML/*.pm
%dir %{perl_vendorarch}/auto/HTML
%dir %{perl_vendorarch}/auto/HTML/Parser
%{perl_vendorarch}/auto/HTML/Parser/Parser.bs
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Parser/Parser.so
%{_mandir}/man3/*
