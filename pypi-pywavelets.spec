#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pywavelets
Version  : 1.4.1
Release  : 63
URL      : https://files.pythonhosted.org/packages/6e/d4/008dceeb95fafcf141f39393bdfc10921d0b62a325c2794ac533195a1eb3/PyWavelets-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/d4/008dceeb95fafcf141f39393bdfc10921d0b62a325c2794ac533195a1eb3/PyWavelets-1.4.1.tar.gz
Summary  : PyWavelets, wavelet transform module
Group    : Development/Tools
License  : MIT
Requires: pypi-pywavelets-license = %{version}-%{release}
Requires: pypi-pywavelets-python = %{version}-%{release}
Requires: pypi-pywavelets-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(docutils)
BuildRequires : pypi(matplotlib)
BuildRequires : pypi(numpy)
BuildRequires : pypi(numpydoc)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
+---------------+-----------------+
| Service       | Master branch   |
+===============+=================+
| Travis        | |travis_ci|     |
+---------------+-----------------+
| Appveyor      | |appveyor_ci|   |
+---------------+-----------------+
| Read the Docs | |read_the_docs| |
+---------------+-----------------+

%package license
Summary: license components for the pypi-pywavelets package.
Group: Default

%description license
license components for the pypi-pywavelets package.


%package python
Summary: python components for the pypi-pywavelets package.
Group: Default
Requires: pypi-pywavelets-python3 = %{version}-%{release}

%description python
python components for the pypi-pywavelets package.


%package python3
Summary: python3 components for the pypi-pywavelets package.
Group: Default
Requires: python3-core
Provides: pypi(pywavelets)
Requires: pypi(docutils)
Requires: pypi(matplotlib)
Requires: pypi(numpy)
Requires: pypi(numpydoc)

%description python3
python3 components for the pypi-pywavelets package.


%prep
%setup -q -n PyWavelets-1.4.1
cd %{_builddir}/PyWavelets-1.4.1
pushd ..
cp -a PyWavelets-1.4.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695154784
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pywavelets
cp %{_builddir}/PyWavelets-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pywavelets/5281e9c932bfeeb26d9b74e98d9deecd806816a0 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pywavelets/5281e9c932bfeeb26d9b74e98d9deecd806816a0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
