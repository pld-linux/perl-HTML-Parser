%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Parser
Summary:	Perl HTML::Parser module
Summary(cs):	Modul pro parsov�n� HTML v Perlu
Summary(da):	HTML::Parser modul til Perl
Summary(de):	HTML::Parser Modul f�r Perl
Summary(es):	M�dulo HTML::Parser para Perl
Summary(fr):	Module HTML::Parser pour Perl
Summary(it):	Modulo HTML::Parser per Perl
Summary(ja):	Perl �� HTML::Parser
Summary(ko):	���� ���� HTML::Parser ����
Summary(pl):	Modu� Perla HTML::Parser
Summary(pt):	O m�dulo HTML::Parser para o Perl
Summary(pt_BR):	M�dulo Perl HTML::Parser
Summary(ru):	HTML::Parser - ����� ������� ��� "�������" HTML-����������
Summary(sv):	HTML::Parser-modul till Perl
Summary(uk):	HTML::Parser - ��¦� ����̦� ��� ������� HTML-�������Ԧ�
Summary(zh_CN):	Perl �� HTML ������ģ�顣
Name:		perl-HTML-Parser
Version:	3.27
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildConflicts:	perl-HTML-Stream = 1.45-3
BuildRequires:	perl-HTML-Tagset
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# HTTP::Headers (perl-libwww) is not always required
%define		_noautoreq	"perl(HTTP::Headers)"

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
Modu� Perla HTML::Parser pozwalaj�cy na parsowanie i wyciaganie
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