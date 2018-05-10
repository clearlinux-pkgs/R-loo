#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-loo
Version  : 2.0.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/loo_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/loo_2.0.0.tar.gz
Summary  : Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian
Group    : Development/Tools
License  : GPL-3.0
Requires: R-matrixStats
BuildRequires : R-matrixStats
BuildRequires : clr-R-helpers

%description
for Bayesian models fit using Markov chain Monte Carlo. The approximation
    uses Pareto smoothed importance sampling (PSIS), a new procedure for
    regularizing importance weights. As a byproduct of the calculations, we also
    obtain approximate standard errors for estimated predictive errors and for
    the comparison of predictive errors between models. The package also 
    provides methods for using stacking and other model weighting techniques 
    to average Bayesian predictive distributions.

%prep
%setup -q -c -n loo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523730033

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523730033
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library loo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library loo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library loo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library loo|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/loo/CITATION
/usr/lib64/R/library/loo/DESCRIPTION
/usr/lib64/R/library/loo/INDEX
/usr/lib64/R/library/loo/Meta/Rd.rds
/usr/lib64/R/library/loo/Meta/data.rds
/usr/lib64/R/library/loo/Meta/features.rds
/usr/lib64/R/library/loo/Meta/hsearch.rds
/usr/lib64/R/library/loo/Meta/links.rds
/usr/lib64/R/library/loo/Meta/nsInfo.rds
/usr/lib64/R/library/loo/Meta/package.rds
/usr/lib64/R/library/loo/Meta/vignette.rds
/usr/lib64/R/library/loo/NAMESPACE
/usr/lib64/R/library/loo/NEWS.md
/usr/lib64/R/library/loo/R/loo
/usr/lib64/R/library/loo/R/loo.rdb
/usr/lib64/R/library/loo/R/loo.rdx
/usr/lib64/R/library/loo/R/sysdata.rdb
/usr/lib64/R/library/loo/R/sysdata.rdx
/usr/lib64/R/library/loo/data/Rdata.rdb
/usr/lib64/R/library/loo/data/Rdata.rds
/usr/lib64/R/library/loo/data/Rdata.rdx
/usr/lib64/R/library/loo/doc/index.html
/usr/lib64/R/library/loo/doc/loo2-example.R
/usr/lib64/R/library/loo/doc/loo2-example.Rmd
/usr/lib64/R/library/loo/doc/loo2-example.html
/usr/lib64/R/library/loo/doc/loo2-weights.R
/usr/lib64/R/library/loo/doc/loo2-weights.Rmd
/usr/lib64/R/library/loo/doc/loo2-weights.html
/usr/lib64/R/library/loo/doc/loo2-with-rstan.R
/usr/lib64/R/library/loo/doc/loo2-with-rstan.Rmd
/usr/lib64/R/library/loo/doc/loo2-with-rstan.html
/usr/lib64/R/library/loo/help/AnIndex
/usr/lib64/R/library/loo/help/aliases.rds
/usr/lib64/R/library/loo/help/figures/stanlogo.png
/usr/lib64/R/library/loo/help/loo.rdb
/usr/lib64/R/library/loo/help/loo.rdx
/usr/lib64/R/library/loo/help/paths.rds
/usr/lib64/R/library/loo/html/00Index.html
/usr/lib64/R/library/loo/html/R.css
