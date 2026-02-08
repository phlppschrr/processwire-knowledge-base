# WireDatabaseBackup::setDatabaseConfig()

Source: `wire/core/WireDatabaseBackup.php`

Set the database configuration information


@param array|Config|object $config Containing these properties:
 - dbUser
 - dbHost
 - dbPort
 - dbName
	- dbPass
 - dbPath (optional)
 - dbCharset (optional)

@return $this

@throws \Exception if missing required config settings
