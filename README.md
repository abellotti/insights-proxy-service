# Installing Insights-Proxy

### Using the official RPM

Using the `insights-proxy` service controller, ***all commands*** for installing and interacting with Insights-Proxy should be executed as a *regular non-root* user. 

To use the service controller to install and manage the Insights-Proxy service, first install the controller:

You need to first enable the latest build [COPR build repo](https://copr.fedorainfracloud.org/coprs/abellott/insights-proxy-service-latest). Example here showing enabling the x86_64 repo for RHEL 9:

```sh
# sudo dnf copr enable abellott/insights-proxy-service-latest rhel-9-x86_64
# sudo dnf config-manager --set-enabled copr:copr.fedorainfracloud.org:abellott:insights-proxy-service-latest
```

Available repositories for insights-proxy include:

- rhel-9-x86_64
- rhel-9-aarch64
- fedora-39-x86_64
- fedora-39-aarch64
- fedora-40-x86_64
- fedora-40-aarch64


Then, install the latest insights-proxy.

```sh
# sudo dnf install -y insights-proxy
```

You must then run the insights-proxy service controller as a regular non-root user of the system.

Install the Insights-Proxy service:

```
$ insights-proxy install
```

Required before starting the Insights-Proxy service for pulling down the
service image from Quay.io:

```
$ podman login quay.io  
```


Start the Insights-Proxy service:
```
$ insights-proxy start
```

Display status of the Insights-Proxy service:
```
$ insights-proxy status
```

To allow external access to the Insights proxy, run the following commands:

```sh
# sudo firewall-cmd --permanent --add-port=3128/tcp 
# sudo firewall-cmd --permanent --add-port=8443/tcp
# sudo firewall-cmd --reload
```

A few seconds later, you may proxy-forward Red-Hat Insights traffic to http://\<server-hosting-the-proxy\>:3128

When running Insights-Proxy, a self-signed certificate is created for accessing any resources served by the proxy 
nd is stored in the host's `~/.local/share/insights-proxy/certs/` directory. You may provide your own
HTTPS certificate and key in this location before starting the Insights-Proxy:

- `~/.local/share/insights-proxy/certs/insights-proxy.crt`
- `~/.local/share/insights-proxy/certs/insights-proxy.key`

The web server part of the insights proxy can be accessed at https://\<server-hosting-the-proxy\>:8443

The download content area for the Insights-Proxy web server is located in the following location:

- `~/.local/share/insights-proxy/download/`

The usage of the insights-proxy service controller is included here below:

```
Usage: insights-proxy [-v | --verbose] <command>

Where <command> is one of:
  install                  - Install Insights-Proxy
  uninstall [-f]           - Uninstall Insights-Proxy
                             specify -f to force remove the certs and download data
  start                    - Start the Insights-Proxy Service
  stop                     - Stop the Insights-Proxy Service
  restart                  - Re-start the Insights-Proxy Service
  status                   - Display Status of the Insights-Proxy Service
```

### Updating the Insights-Proxy configuration

The configuration of the Insights-Proxy can be updated as follows:

- update the Insights Proxy parameters in `~/.config/insights-proxy/env/insights-provy.env` 
- you can also update the list of allowed upstream servers in `~/.config/insigihts-proxy/env/insights-proxy.servers`

then restart the service:

```
$ insights-proxy restart
```

The configuration parameters include:

- `INSIGHTS_PROXY_DISABLE` to disable the forward proxying, _defaults to 0_
- `INSIGHTS_PROXY_DEBUG_CONFIG` to log environment variable and Nginx configuration upon startup, _defaults to 0_
- `INSIGHTS_PROXY_SERVICE_PORT` to define the listening port of the forward proxy, _defaults to 3128_
- `INSIGHTS_PROXY_DNS_SERVER` to define which DNS server to use for name resolution, _defaults to 8.8.8.8_
- `INSIGHTS_WEB_SERVER_DISABLE` to disable the insights proxy web server, _defaults to 0_
- `INSIGHTS_WEB_SERVER_PORT` to define the listening port of the insights proxy web server, _defaults to 8443_



