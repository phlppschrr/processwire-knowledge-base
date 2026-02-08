# $database->__construct($host = 'localhost', $user = null, $pass = null, $db = null, $port = null, $socket = null)

Source: `wire/core/Database.php`

Construct the Database

Since this extends MySQL all the MySQL construct params are kept in tact.
However, you may just supply an object with the following properties if you prefer:
$o->dbUser, $o->dbPass, $o->dbHost, $o->dbName, $config->dbPort, $config->dbSocket (optional).
This would usually be from a ProcessWire Config ($config) API var, but kept as generic object
in case someone wants to use this class elsewhere.

## Arguments

- `$host` (optional) `string|Config` Hostname or object with config properties.
- `$user` (optional) `string` Username
- `$pass` (optional) `string` Password
- `$db` (optional) `string` Database name
- `$port` (optional) `int` Port
- `$socket` (optional) `string` Socket

## Throws

- WireDatabaseException
