<<<<<<< HEAD
#! /usr/bin/env puppet
#  Ensure python3-pip is installed
package { 'python3-pip':
 ensure => installed,
}

package { 'flask':
 ensure   => '2.1.0',
 provider => pip3,
 require => Package['python3-pip'],
}

package { 'werkzeug':
 ensure   => '2.0.1',
 provider => pip,
 require => Package['python3-pip'],
=======
#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
>>>>>>> 4913a65a7734968cc129cf8c7d7d7c0f0411e5de
}
