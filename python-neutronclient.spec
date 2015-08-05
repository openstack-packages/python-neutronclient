Name:       python-neutronclient
Version:    XXX
Release:    XXX
Summary:    Python API and CLI for OpenStack Neutron

License:    ASL 2.0
URL:        http://launchpad.net/python-neutronclient/
Source0:    https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-d2to1

Requires: pyparsing
Requires: python-cliff >= 1.0
Requires: python-keystoneclient >= 0.9.0
Requires: python-oslo-i18n
Requires: python-oslo-serialization
Requires: python-oslo-utils
Requires: python-pbr
Requires: python-prettytable >= 0.6
Requires: python-requests
Requires: python-setuptools
Requires: python-simplejson


%description
Client library and command line utility for interacting with Openstack
Neutron's API.

%prep
%setup -q -n %{name}-%{upstream_version}

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Install other needed files
install -p -D -m 644 tools/neutron.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/neutron.bash_completion

# Remove unused files
rm -rf %{buildroot}%{python_sitelib}/neutronclient/tests

%files
%license LICENSE
%doc README.rst
%{_bindir}/neutron
%{python2_sitelib}/neutronclient
%{python2_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d

%changelog
