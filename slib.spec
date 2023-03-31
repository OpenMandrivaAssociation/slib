Summary:	Platform independent library for scheme
Name:		slib
Version:	3b6
Release:	2
License:	SLIB
Group:		Development/Other
BuildArch:	noarch
Source0:	https://ftp.gnu.org/gnu/slib/%{name}-%{version}.tar.gz
URL:		http://people.csail.mit.edu/jaffer/SLIB.html

%description
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accommodate packages specific to a site,
implementation, user, or directory.

%prep
%autosetup -p1
sed -r -i "s,/usr/(local/)?lib/slib,%{_datadir}/slib,g" *.init

%build

%install
mkdir -p %{buildroot}%{_datadir}/slib
cp *.scm *.init *.xyz *.txt *.dat *.ps %{buildroot}%{_datadir}/slib
mkdir -p %{buildroot}%{_infodir}
install -m644 slib.info %{buildroot}%{_infodir}

%files
%doc ANNOUNCE README COPYING FAQ ChangeLog
%{_datadir}/slib
%{_infodir}/slib.*
