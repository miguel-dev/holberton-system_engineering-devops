# Sets limit higher to open files for working process.
exec { 'higher limit':
  command => 'sudo sed -i "s/15/8000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/bin/:/bin/',
}
