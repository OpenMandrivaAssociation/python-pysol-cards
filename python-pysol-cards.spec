%global __requires_exclude testtools
%global pypi_name pysol-cards

Name:           python-%{pypi_name}
Version:        0.24.0
Release:        2
Summary:        Deal PySol FC Cards
Group:          Development/Python
License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pysol_cards-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
The pysol-cards python modules allow the python developer to generate the
initial deals of some PySol FC games.

%prep
%autosetup -n pysol_cards-0.24.0
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py_install

%files
%license LICENSE
%doc README*
%{python_sitelib}/pysol_cards
%{python_sitelib}/pysol_cards-%{version}-py*.*.egg-info
