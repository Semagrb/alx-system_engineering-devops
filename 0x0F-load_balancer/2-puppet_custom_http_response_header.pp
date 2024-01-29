# Puppet script for configuring NGINX with a custom HTTP header response

# Step 1: Update package information
exec {'update':
  command => '/usr/bin/apt-get update',
}

# Step 2: Install NGINX package
-> package {'nginx':
  ensure => 'present',
}

# Step 3: Add a custom HTTP header to NGINX configuration
# This sets the 'X-Served-By' header to the hostname of the server
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

# Step 4: Start the NGINX service
exec {'run2':
  command => '/usr/sbin/service nginx start',
}
