%define		perl_sitelib   %(eval "`perl -V:installsitelib`"; echo $installsitelib)

Summary:	Perl HTML-Parser module
Summary(pl):	Modu³ Perla HTML-Parser
Name:		perl-HTML-Parser
Version:	2.23
Release:	0.1
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML-Parser-%{version}.tar.gz
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Perl HTML-Parser module

%description -l pl
Modu³ perla pozwalaj±cy analizowaæ pliki HTML.

%prep
%setup -q -n HTML-Parser-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_sitearch} \
	$RPM_BUILD_ROOT%{_mandir}/man3 \
	$RPM_BUILD_ROOT/%{perl_archlib}

make \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
	install

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
%dir %{perl_sitelib}/HTML
%{perl_sitelib}/HTML/*.pm

%{perl_sitearch}/auto/HTML

%{_mandir}/man3/*
