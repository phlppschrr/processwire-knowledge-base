# $wireDatabaseBackup->__construct($path = '')

Source: `wire/core/WireDatabaseBackup.php`

Construct

You should follow-up the construct call with one or both of the following:

	- $backups->setDatabase(PDO|WireDatabasePDO);
	- $backups->setDatabaseConfig(array|object);

## Arguments

- string $path Path where database files are stored

## Throws

- \Exception
