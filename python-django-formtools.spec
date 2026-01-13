%define module django-formtools
%define oname django_formtools
%bcond tests 1

Name:		python-django-formtools
Version:	2.5.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A set of high-level abstractions for Django forms
URL:		https://pypi.org/project/django-formtools/
License:	BSD-3-Clause
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(django)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(wheel)

%description
A set of high-level abstractions for Django forms

%package -n python-%{module}-doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description -n python-%{module}-doc
Documentation for the %{name} package.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%install
%py_install
# Fix doc build with latest Sphinx, see https://github.com/jazzband/django-formtools/issues/279
sed -i "s#'http://docs.python.org/': None#'python': ('https://docs.python.org/3', None)#" docs/conf.py
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if %{with tests}
%check
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=`pwd`
%{__python} -m django test -v 2 tests --pythonpath=`pwd`
%endif

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/formtools
%{python_sitelib}/tests/wizard
%{python_sitelib}/%{oname}-%{version}.dist-info

%files -n python-%{module}-doc
%doc html
%license LICENSE
