#Replaces phpp for php                                                                
exec { 'replace':
    path    => ['/bin', '/usr/bin'],
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php; sudo service apac
he2 restart;',
}
