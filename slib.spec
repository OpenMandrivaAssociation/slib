Summary:      Platform independent library for scheme
Name:         slib
Version:      3b3
Release:      5
License:      SLIB
Group:        Development/Other
BuildArch:    noarch
Source0:      http://groups.csail.mit.edu/mac/ftpdir/scm/slib-%{version}.zip
URL:          http://people.csail.mit.edu/jaffer/SLIB.html

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
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/slib
cp *.scm *.init *.xyz *.txt *.dat *.ps ${RPM_BUILD_ROOT}%{_datadir}/slib
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
install -m644 slib.info $RPM_BUILD_ROOT%{_infodir}

%files
%defattr(-,root,root)
%doc ANNOUNCE README COPYING FAQ ChangeLog
%{_datadir}/slib
%{_infodir}/slib.*


%changelog
* Fri Mar 18 2011 Jani Välimaa <wally@mandriva.org> 3b3-1mdv2011.0
+ Revision: 646374
- new version 3b3

* Tue Jul 27 2010 Götz Waschk <waschk@mandriva.org> 3b2-2mdv2011.0
+ Revision: 561020
- rebuild to replace the 2010.0 update (bug #60295)

* Thu Feb 18 2010 Frederic Crozat <fcrozat@mandriva.com> 3b2-1mdv2010.1
+ Revision: 507815
- Release 3b2 (fixes Mdv bug #42526)
- Update urls
- sync with fedora

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3a4-4mdv2010.0
+ Revision: 427185
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3a4-3mdv2009.1
+ Revision: 351514
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3a4-2mdv2009.0
+ Revision: 225444
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 26 2007 Frederic Crozat <fcrozat@mandriva.com> 3a4-1mdv2008.1
+ Revision: 113029
- import slib


