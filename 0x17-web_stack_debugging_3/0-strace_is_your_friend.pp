#Replaces phpp for php
exec { 'replace':
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php;',
}
