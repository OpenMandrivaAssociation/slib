Summary:      Platform independent library for scheme
Name:         slib
Version:      3a4
Release:      %mkrel 1
License:      SLIB
Group:        Development/Other
BuildArch:    noarch
Source0:      ftp://swissnet.ai.mit.edu/pub/scm/slib%{version}.tar.gz
Patch1:       slib-3a4-guile.patch
URL:          http://swissnet.ai.mit.edu/~jaffer/SLIB.html
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
%patch1 -p1 -b .guile
for i in *; do
  sed -e "s,/usr/local/lib,%{_datadir},g" \
      -e "s,/usr/lib,%{_datadir},g" \
      -e "s,/usr/local,/usr,g" < "${i}" > "${i}.tmp"
  mv "${i}.tmp" "${i}"
done

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/slib
cp *.scm *.init *.xyz *.txt *.dat *.ps ${RPM_BUILD_ROOT}%{_datadir}/slib
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
install -m644 slib.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%_install_info slib.info

%preun
%_remove_install_info slib.info

%files
%defattr(-,root,root)
%dir %{_datadir}/slib
%doc ANNOUNCE README COPYING FAQ ChangeLog
%{_datadir}/slib/*
%{_infodir}/slib.*

