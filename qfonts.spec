Summary:	True Type Quasi Fonts
Summary(pl):	Fonty Quasi w formacie True Type
Name:		qfonts
Version:	1.07
Release:	2
License:	GPL
Group:		Fonts
Source0:	ftp://ftp.gust.org.pl/TeX/GUST/contrib/fonts/qfonts/qfnt-tds.zip
# Source0-md5:	2ee92d9e1a174b66de3a17739e3cd3c9
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains collection of following True Type fonts:
- QuasiBookman (see 0readme.qbk.gz)
- QuasiChancery (see 0readme.qch.gz)
- QuasiCourier (see 0readme.qco.gz)
- QuasiHelvetica (see 0readme.qhv.gz)
- QuasiHelveticaCondensed (see 0readme.qhv.gz)

%description -l pl
Pakiet ten zawiera nastêpuj±ce fonty w formacie True Type:
- QuasiBookman (zobacz 0readme.qbk.gz)
- QuasiChancery (zobacz 0readme.qch.gz)
- QuasiCourier (zobacz 0readme.qco.gz)
- QuasiHelvetica (zobacz 0readme.qhv.gz)
- QuasiHelveticaCondensed (zobacz 0readme.qhv.gz)

%prep
%setup -q -T -c -n qfonts
unzip -qa %{SOURCE0}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF

install texmf/fonts/truetype/public/qfonts/*.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc texmf/doc/fonts/polish/qfonts/*
%{_fontsdir}/TTF/*
