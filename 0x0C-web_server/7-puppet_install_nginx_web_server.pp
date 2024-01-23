#!/usr/bin/env bash
# Configure Nginx server using Puppet

# Defines a Puppet class called nginx_server that encapsulates the configuration for the Nginx server.
class nginx_server {
  # Ensures that the Nginx package is installed.
  package { 'nginx':
    ensure => installed,
  }

  # Manages the Nginx service, ensuring it is running and enabled.
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  # Manages the Nginx configuration file located at /etc/nginx/sites-available/default.
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
      server {
        listen      80 default_server;
        listen      [::]:80 default_server;
        root        /var/www/html;
        index       index.html index.htm;

        # Configures the root path to return 'Hello World!'
        location / {
          return 200 'Hello World!';
        }

        # Configures the /redirect_me path to return a 301 redirection to http://cuberule.com/
        location /redirect_me {
          return 301 http://cuberule.com/;
        }
      }
    ",
    notify => Service['nginx'],
  }
}

# Includes the nginx_server class, ensuring that it gets applied.
include nginx_server
