# Database::__construct()

Source: `wire/core/Database.php`

Construct the Database

Since this extends MySQL all the MySQL construct params are kept in tact.
However, you may just supply an object with the following properties if you prefer:
$o->dbUser, $o->dbPass, $o->dbHost, $o->dbName, $config->dbPort, $config->dbSocket (optional).
This would usually be from a ProcessWire Config ($config) API var, but kept as generic object
in case someone wants to use this class elsewhere.

@param string|Config $host Hostname or object with config properties.

@param string $user Username

@param string $pass Password

@param string $db Database name

@param int $port Port

@param string $socket Socket

@throws WireDatabaseException
