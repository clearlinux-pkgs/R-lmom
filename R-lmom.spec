#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lmom
Version  : 2.8
Release  : 4
URL      : https://cran.r-project.org/src/contrib/lmom_2.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lmom_2.8.tar.gz
Summary  : L-Moments
Group    : Development/Tools
License  : Common
Requires: R-lmom-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
and trimmed L-moments of distributions and data samples; parameter
  estimation; L-moment ratio diagram; plot vs. quantiles of an
  extreme-value distribution.

%package lib
Summary: lib components for the R-lmom package.
Group: Libraries

%description lib
lib components for the R-lmom package.


%prep
%setup -q -c -n lmom
cd %{_builddir}/lmom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610381097

%install
export SOURCE_DATE_EPOCH=1610381097
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmom
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lmom || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lmom/CITATION
/usr/lib64/R/library/lmom/DESCRIPTION
/usr/lib64/R/library/lmom/INDEX
/usr/lib64/R/library/lmom/Meta/Rd.rds
/usr/lib64/R/library/lmom/Meta/features.rds
/usr/lib64/R/library/lmom/Meta/hsearch.rds
/usr/lib64/R/library/lmom/Meta/links.rds
/usr/lib64/R/library/lmom/Meta/nsInfo.rds
/usr/lib64/R/library/lmom/Meta/package.rds
/usr/lib64/R/library/lmom/NAMESPACE
/usr/lib64/R/library/lmom/NEWS
/usr/lib64/R/library/lmom/R/lmom
/usr/lib64/R/library/lmom/R/lmom.rdb
/usr/lib64/R/library/lmom/R/lmom.rdx
/usr/lib64/R/library/lmom/help/AnIndex
/usr/lib64/R/library/lmom/help/aliases.rds
/usr/lib64/R/library/lmom/help/lmom.rdb
/usr/lib64/R/library/lmom/help/lmom.rdx
/usr/lib64/R/library/lmom/help/paths.rds
/usr/lib64/R/library/lmom/html/00Index.html
/usr/lib64/R/library/lmom/html/R.css
/usr/lib64/R/library/lmom/lmom-manual.pdf

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lmom/libs/lmom.so
/usr/lib64/R/library/lmom/libs/lmom.so.avx2
/usr/lib64/R/library/lmom/libs/lmom.so.avx512
