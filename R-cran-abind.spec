%define modulename abind
%define realver 1.1-0
%define r_library %{_libdir}/R/library

Summary:	Combine multi-dimensional arrays for R
Name:		R-cran-%{modulename}
Version:	%(echo %realver|tr '-' '.')
Release:	%mkrel 6
License:	LGPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Combine multi-dimensional arrays.This is a generalization of 
cbind and rbind.Takes a sequence of vectors, matrices, or arrays 
and produces a single array of the same or higher dimension.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
