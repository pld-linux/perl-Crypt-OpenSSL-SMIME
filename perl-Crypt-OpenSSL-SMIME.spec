#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-SMIME
Summary:	Crypt::OpenSSL::SMIME - signing and encrypting using OpenSSL S/MIME functions
Summary(pl):	Crypt::OpenSSL::SMIME - podpisywanie i szyfrowanie z u¿yciem funkcji S/MIME OpenSSL
Name:		perl-Crypt-OpenSSL-SMIME
Version:	0.02
Release:	1
License:	OpenSSL (Apache-style)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	186d6cb4dcffa7f8b89699552de7750d
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::SMIME is a Perl module for signing and encrypting
messages with S/MIME standard using OpenSSL libraries. It's useful
for sending sensitive information to Mozilla or Outlook users
without additional software as PGP.

%description -l pl
Crypt::OpenSSL::SMIME to modu³ Perla do podpisywana i szyfrowania
wiadomo¶ci zgodnie ze standardem S/MIME z u¿yciem bibliotek OpenSSL.
Jest przydatny do wysy³ania poufnych informacji do u¿ytkowników
Mozilli lub Outlooka nie maj±cych dodatkowego oprogramowania typu
PGP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's/.*MAN.PODS.*//' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/Crypt/OpenSSL/SMIME.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/SMIME
%{perl_vendorarch}/auto/Crypt/OpenSSL/SMIME/autosplit.ix
%{perl_vendorarch}/auto/Crypt/OpenSSL/SMIME/SMIME.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/SMIME/SMIME.so
%{_mandir}/man3/*
