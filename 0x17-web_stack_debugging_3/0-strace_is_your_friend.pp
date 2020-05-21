#Replaces phpp for php                                                                
exec { 'replace':
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php; sudo service apac
    path    => ['/bin', '/usr/bin'],
he2 restart;',
}
