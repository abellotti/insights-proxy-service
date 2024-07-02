Name:           insights-proxy
Version:        1.2
Release:        1%{?dist}
Summary:        Insights Proxy Serice v1.2

License:        GPLv3
URL:            https://gihub.com/abellotti/insights-proxy-service
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       bash

%description
This RPM installs the Insights Proxy Service v1.2 on the System.
The Insights Proxy service controller installs and manages
the Insights Proxy v1.2 via a systemd quadlet service.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/bin
cp bin/%{name} %{buildroot}/%{_bindir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/config
cp config/*.container %{buildroot}/%{_datadir}/%{name}/config/
mkdir -p %{buildroot}/%{_datadir}/%{name}/env
cp env/*.env %{buildroot}/%{_datadir}/%{name}/env/
cp env/*.servers %{buildroot}/%{_datadir}/%{name}/env/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/config/insights-proxy.container
%{_datadir}/%{name}/env/insights-proxy.env
%{_datadir}/%{name}/env/insights-proxy.servers

%changelog
* Tue Jul 02 2024 Alberto Bellotti <abellott@redhat.com>
- Version 1.2
- Adding support for

* Fri Jun 28 2024 Alberto Bellotti <abellott@redhat.com>
- Version 1.1
- Initial prototype
