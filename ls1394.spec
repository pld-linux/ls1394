Summary:	List 1394 (Firewire) Devices
Summary(pl.UTF-8):	Wypisywanie urządzeń 1394 (Firewire)
Name:		ls1394
Version:	20070103
Release:	1
License:	GPL
Group:		Applications
Source0:	http://me.in-berlin.de/~s5r6/linux1394/ls1394/ls1394_v%{version}
# Source0-md5:	0764d5f0b6e5ac0addb519d05b1fcac5
Source1:	oui.db
URL:		http://me.in-berlin.de/~s5r6/linux1394/ls1394/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lists 1394 (Firewire) devices.

%description -l pl.UTF-8
Narzędzie wypisujące urządzenia 1394 (Firewire).

%prep
%setup -q -c -T
cp %{SOURCE0} %{name}

%install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/misc}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/misc/oui.db

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/misc/oui.db
