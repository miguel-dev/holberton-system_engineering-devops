#Creates a manifest that kills a process named killmenow
exec { 'manifest for killing killmenow':
  command => '/usr/bin/pkill --full killmenow'
}
