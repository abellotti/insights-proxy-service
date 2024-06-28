Name:           insights-proxy
Version:        1.1
Release:        1%{?dist}
Summary:        Insights Proxy Serice v1.1

License:        GPLv3
URL:            https://gihub.com/abellotti/insights-proxy
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       bash

%description
This RPM installs the Insights Proxy Service v1.1 on the System.
The Insights Proxy management tool installs and configures Insighs Proxy v1.1
to be managed and run as a systemd quadlet service.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/bin
cp installer/bin/%{name} %{buildroot}/%{_bindir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/config
cp installer/config/*.container %{buildroot}/%{_datadir}/%{name}/config/
mkdir -p %{buildroot}/%{_datadir}/%{name}/env
cp installer/env/*.env %{buildroot}/%{_datadir}/%{name}/env/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/config/insights-proxy.container
%{_datadir}/%{name}/env/insights-proxy.env

%changelog
* Thu Jun 26 2024 Alberto Bellotti <abellott@redhat.com>
1.1
