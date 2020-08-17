%global pypi_name pysol-cards

Name:           python-%{pypi_name}
Version:        0.10.1
Release:        %mkrel 1
Summary:        Deal PySol FC Cards
Group:          Development/Python
License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pysol_cards-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildConflicts: python3dist(coverage) = 4.4
BuildRequires:  python3dist(coverage) >= 4.0
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pbr) >= 2.0
BuildRequires:  python3dist(python-subunit) >= 0.0.18
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(testtools) >= 1.4.0
BuildRequires:  python3dist(sphinx)

%description
The pysol-cards python modules allow the python developer to generate the
initial deals of some PySol FC games.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The pysol-cards python modules allow the python developer to generate the
initial deals of some PySol FC games.

%prep
%autosetup -n pysol_cards-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/pysol_cards
%{python3_sitelib}/pysol_cards-%{version}-py?.?.egg-info
