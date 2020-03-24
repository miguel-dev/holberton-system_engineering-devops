# Execute a command
exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin/pkill',
}
