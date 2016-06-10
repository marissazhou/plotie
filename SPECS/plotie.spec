%define artifact_name plotie
%define current_directory %(echo $PWD)
%define unmangled_version %(hero describe rpm version)
%define release %(hero describe rpm release)
%define python_version %(python --version 2>&1 | cut -d. -f1,2 | sed 's/ //' | tr A-Z a-z)
%define summary plotie

Summary: %{summary}
Name: %{artifact_name}
Version: %{unmangled_version}
Release: %{release}
Source0: %{artifact_name}-%{unmangled_version}
License: Commercial
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Requires: python-setuptools lrms-bash-profile lrms-namedentities
Provides: %{artifact_name}
Vendor: Propylon
AutoReqProv: no

%description
%{summary}

%prep
rm -rf %{SOURCE0}
rsync -ra --exclude='SOURCES/' --exclude='.env*/' %{current_directory}/ %{SOURCE0}/

%build
cd %{SOURCE0}
%{python_version} setup.py build
cd docs
rm -rf _build
rm -rf build
make clean && make man
cd ..

%install
cd %{SOURCE0}
mkdir -p %{buildroot}%{_mandir}/man1/
%{python_version} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=PYTHON_INSTALLED_FILES --prefix=/opt/lrms
cat PYTHON_INSTALLED_FILES > INSTALLED_FILES

cp %{SOURCE0}/docs/build/man/plotie.1* %{buildroot}%{_mandir}/man1/

for f in $(ls %{buildroot}/opt/lrms/bin/ || :)
do
  sed -i 's|#!.*|#!/usr/bin/env python|' "%{buildroot}/opt/lrms/bin/$f"
done

%clean
rm -rf %{_sourcedir}/*
rm -rf %{_builddir}/*
rm -rf %{buildroot}/*
rm -rf %{_srcrpmdir}/*

%files -f %{SOURCE0}/INSTALLED_FILES
%{_mandir}/man1/plotie-1*
%defattr(-,root,root)

%changelog
%(hero describe rpm changelog)
