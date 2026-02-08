# WireDatabaseBackup::__construct()

Source: `wire/core/WireDatabaseBackup.php`

Construct

You should follow-up the construct call with one or both of the following:

	- $backups->setDatabase(PDO|WireDatabasePDO);
	- $backups->setDatabaseConfig(array|object);


@param string $path Path where database files are stored

@throws \Exception
