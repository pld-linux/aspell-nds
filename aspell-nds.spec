Summary:	Low Saxon dictionary for aspell
Summary(pl.UTF-8):	Słownik dolnosaksoński dla aspella
Name:		aspell-nds
Version:	0.01
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/nds/aspell6-nds-%{version}-%{subv}.tar.bz2
# Source0-md5:	76b2b3f2bdeefdfc6ce75ae11c9ae149
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low Saxon dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik dolnosaksoński (lista słów) dla aspella.

%prep
%setup -q -n aspell6-nds-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
