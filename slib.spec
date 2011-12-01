Summary:      Platform independent library for scheme
Name:         slib
Version:      3b3
Release:      %mkrel 1
License:      SLIB
Group:        Development/Other
BuildArch:    noarch
Source0:      http://groups.csail.mit.edu/mac/ftpdir/scm/slib-%{version}.zip
URL:          http://people.csail.mit.edu/jaffer/SLIB.html
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): info-install
Requires(preun): info-install

%description
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accommodate packages specific to a site,
implementation, user, or directory.

%prep
%setup -q -n %{name}
sed -r -i "s,/usr/(local/)?lib/slib,%{_datadir}/slib,g" *.init

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/slib
cp *.scm *.init *.xyz *.txt *.dat *.ps %{buildroot}%{_datadir}/slib
mkdir -p %{buildroot}%{_infodir}
install -m644 slib.info %{buildroot}%{_infodir}

%clean
rm -rf %{buildroot}

%post
%_install_info slib.info

%preun
%_remove_install_info slib.info

%files
%defattr(-,root,root)
%doc ANNOUNCE README COPYING FAQ ChangeLog
%{_datadir}/slib
%{_infodir}/slib.*
