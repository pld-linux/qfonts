Summary:	True Type Quasi Fonts
Summary(pl):	Fonty Quasi w formacie True Type
Name:		qfonts
Version:	1.05
Release:	1
License:	GPL
Group:		X11/Fonts
Group(de):	X11/Fonts
Group(pl):	X11/Fonty
Source0:	ftp://ftp.gust.org.pl:/TeX/GUST/contrib/fonts/qfonts/qfnt-tds.zip
BuildRequires:	unzip
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
%setup  -q -T -c -n qfonts
unzip -qa %{SOURCE0}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF

install texmf/fonts/truetype/public/qfonts/*.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

gzip -9nf texmf/doc/fonts/polish/qfonts/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc texmf/doc/fonts/polish/qfonts/*.gz
%{_fontsdir}/TTF/*
