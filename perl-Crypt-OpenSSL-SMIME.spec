#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	OpenSSL-SMIME
Summary:	Crypt::OpenSSL::SMIME - signing and encrypting using OpenSSL S/MIME functions
Summary(pl.UTF-8):	Crypt::OpenSSL::SMIME - podpisywanie i szyfrowanie z użyciem funkcji S/MIME OpenSSL
Name:		perl-Crypt-OpenSSL-SMIME
Version:	0.05
Release:	1
License:	OpenSSL (Apache-like)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e5b1b0fa495d4ce60c02660fd444369c
URL:		http://search.cpan.org/dist/Crypt-OpenSSL-SMIME/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::SMIME is a Perl module for signing and encrypting
messages with S/MIME standard using OpenSSL libraries. It's useful
for sending sensitive information to Mozilla or Outlook users
without additional software as PGP.

%description -l pl.UTF-8
Crypt::OpenSSL::SMIME to moduł Perla do podpisywana i szyfrowania
wiadomości zgodnie ze standardem S/MIME z użyciem bibliotek OpenSSL.
Jest przydatny do wysyłania poufnych informacji do użytkowników
Mozilli lub Outlooka nie mających dodatkowego oprogramowania typu
PGP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's/.*MAN.PODS.*//' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%doc CHANGES README
%{perl_vendorarch}/Crypt/OpenSSL/SMIME.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/SMIME
%{perl_vendorarch}/auto/Crypt/OpenSSL/SMIME/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/SMIME/SMIME.so
%{_mandir}/man3/*
