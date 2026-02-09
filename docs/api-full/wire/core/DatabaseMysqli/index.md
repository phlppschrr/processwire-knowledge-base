# DatabaseMysqli

Source: `wire/core/DatabaseMysqli.php`

## Summary

Temporary wrapper to mysqli Database class for mysqli => PDO transition

This is for temporary use while transitioning from mysqli to PDO

It's entire purpose is to ensure that a $db API variable is available, while not
actually instantiating mysqli (and forming a mysql connection) until the $db
variable is called upon to do something.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/
