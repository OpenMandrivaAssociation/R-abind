%global packname  abind
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.3_0
Release:          1
Summary:          Combine multi-dimensional arrays
Group:            Sciences/Mathematics
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/abind/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/abind/abind_1.3-0.tar.gz
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
rm -rf %{buildroot}
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
