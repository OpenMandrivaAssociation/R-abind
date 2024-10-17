%global packname  abind
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.4_0
Release:          4
Summary:          Combine multi-dimensional arrays
Group:            Sciences/Mathematics
License:          LGPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-0.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%rename R-cran-abind

%description
Combine multi-dimensional arrays into a single array. This is a
generalization of cbind and rbind.  Works with vectors, matrices, and
higher-dimensional arrays.  Also provides functions adrop, asub, and afill
for manipulating, extracting and replacing data in arrays.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4_0-2
+ Revision: 774989
- Use proper tarball.
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3_0-1
+ Revision: 774764
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-6mdv2011.0
+ Revision: 616442
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-5mdv2010.0
+ Revision: 433066
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-4mdv2009.0
+ Revision: 260108
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-3mdv2009.0
+ Revision: 247972
- rebuild

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-1mdv2008.1
+ Revision: 169958
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-abind.

