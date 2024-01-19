#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
class {'python': }
include python::pip

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
