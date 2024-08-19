Name:           insights-proxy
Version:        1.2
Release:        1%{?dist}
Summary:        Insights Proxy Serice v1.2

License:        GPLv3
URL:            https://github.com/abellotti/insights-proxy-service
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       bash

%description
This RPM installs the Insights Proxy Service on the System.
The Insights Proxy service controller installs and manages
the Insights Proxy via a systemd quadlet service.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/bin
cp bin/%{name} %{buildroot}/%{_bindir}/%{name}
cp bin/insights-proxy-configure %{buildroot}/%{_datadir}/%{name}/bin/insights-proxy-configure
mkdir -p %{buildroot}/%{_datadir}/%{name}/config
cp config/*.container %{buildroot}/%{_datadir}/%{name}/config/
mkdir -p %{buildroot}/%{_datadir}/%{name}/env
cp env/*.env %{buildroot}/%{_datadir}/%{name}/env/
cp env/*.servers %{buildroot}/%{_datadir}/%{name}/env/
mkdir -p %{buildroot}/%{_datadir}/%{name}/download/bin
cp download/bin/*.template %{buildroot}/%{_datadir}/%{name}/download/bin/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/bin/insights-proxy-configure
%{_datadir}/%{name}/config/insights-proxy.container
%{_datadir}/%{name}/env/insights-proxy.env
%{_datadir}/%{name}/env/insights-proxy.servers
%{_datadir}/%{name}/download/bin/configure-client.sh.template

%changelog
* Tue Jul 02 2024 Alberto Bellotti <abellott@redhat.com>
- Version 1.2
- Additional enhancements

* Fri Jun 28 2024 Alberto Bellotti <abellott@redhat.com>
- Version 1.1
- Initial prototype
