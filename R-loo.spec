#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-loo
Version  : 2.1.0
Release  : 18
URL      : https://cran.r-project.org/src/contrib/loo_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/loo_2.1.0.tar.gz
Summary  : Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian
Group    : Development/Tools
License  : GPL-3.0
Requires: R-assertthat
Requires: R-cli
Requires: R-withr
BuildRequires : R-assertthat
BuildRequires : R-checkmate
BuildRequires : R-cli
BuildRequires : R-markdown
BuildRequires : R-matrixStats
BuildRequires : R-withr
BuildRequires : R-yaml
BuildRequires : buildreq-R

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
export SOURCE_DATE_EPOCH=1552841699

%install
export SOURCE_DATE_EPOCH=1552841699
rm -rf %{buildroot}
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
R CMD check --no-manual --no-examples --no-codoc  loo || :


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
/usr/lib64/R/library/loo/doc/loo2-lfo.R
/usr/lib64/R/library/loo/doc/loo2-lfo.Rmd
/usr/lib64/R/library/loo/doc/loo2-lfo.html
/usr/lib64/R/library/loo/doc/loo2-non-factorizable.R
/usr/lib64/R/library/loo/doc/loo2-non-factorizable.Rmd
/usr/lib64/R/library/loo/doc/loo2-non-factorizable.html
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
/usr/lib64/R/library/loo/tests/testthat.R
/usr/lib64/R/library/loo/tests/testthat/E_loo_default_mean.rds
/usr/lib64/R/library/loo/tests/testthat/E_loo_default_quantile_10_50_90.rds
/usr/lib64/R/library/loo/tests/testthat/E_loo_default_quantile_50.rds
/usr/lib64/R/library/loo/tests/testthat/E_loo_default_var.rds
/usr/lib64/R/library/loo/tests/testthat/E_loo_matrix_mean.rds
/usr/lib64/R/library/loo/tests/testthat/E_loo_matrix_quantile_10_90.rds
/usr/lib64/R/library/loo/tests/testthat/E_loo_matrix_quantile_50.rds
/usr/lib64/R/library/loo/tests/testthat/E_loo_matrix_var.rds
/usr/lib64/R/library/loo/tests/testthat/compare_three_models.rds
/usr/lib64/R/library/loo/tests/testthat/compare_two_models.rds
/usr/lib64/R/library/loo/tests/testthat/function_method_stuff.R
/usr/lib64/R/library/loo/tests/testthat/gpdfit.rds
/usr/lib64/R/library/loo/tests/testthat/gpdfit_default_grid.rds
/usr/lib64/R/library/loo/tests/testthat/gpdfit_old.rds
/usr/lib64/R/library/loo/tests/testthat/loo.rds
/usr/lib64/R/library/loo/tests/testthat/loo_compare_three_models.rds
/usr/lib64/R/library/loo/tests/testthat/loo_compare_two_models.rds
/usr/lib64/R/library/loo/tests/testthat/mcse_loo.rds
/usr/lib64/R/library/loo/tests/testthat/model_weights_pseudobma.rds
/usr/lib64/R/library/loo/tests/testthat/model_weights_stacking.rds
/usr/lib64/R/library/loo/tests/testthat/psis.rds
/usr/lib64/R/library/loo/tests/testthat/test_0_helpers.R
/usr/lib64/R/library/loo/tests/testthat/test_E_loo.R
/usr/lib64/R/library/loo/tests/testthat/test_compare.R
/usr/lib64/R/library/loo/tests/testthat/test_data_psis_approximate_posterior.rda
/usr/lib64/R/library/loo/tests/testthat/test_deprecated_extractors.R
/usr/lib64/R/library/loo/tests/testthat/test_extract_log_lik.R
/usr/lib64/R/library/loo/tests/testthat/test_gpdfit.R
/usr/lib64/R/library/loo/tests/testthat/test_kfold_helpers.R
/usr/lib64/R/library/loo/tests/testthat/test_loo_and_waic.R
/usr/lib64/R/library/loo/tests/testthat/test_model_weighting.R
/usr/lib64/R/library/loo/tests/testthat/test_print_plot.R
/usr/lib64/R/library/loo/tests/testthat/test_psis.R
/usr/lib64/R/library/loo/tests/testthat/test_psis_approximate_posterior.R
/usr/lib64/R/library/loo/tests/testthat/test_psislw.R
/usr/lib64/R/library/loo/tests/testthat/test_relative_eff.R
/usr/lib64/R/library/loo/tests/testthat/waic.rds
