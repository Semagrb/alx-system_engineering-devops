class {'python': }
include python::pip

package { 'Flask':
 ensure   => '2.1.0',
 provider => 'pip',
}
