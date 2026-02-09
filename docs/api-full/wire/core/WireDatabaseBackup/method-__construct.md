# $wireDatabaseBackup->__construct($path = '')

Source: `wire/core/WireDatabaseBackup.php`

Construct

You should follow-up the construct call with one or both of the following:

	- $backups->setDatabase(PDO|WireDatabasePDO);
	- $backups->setDatabaseConfig(array|object);

## Usage

~~~~~
// basic usage
$result = $wireDatabaseBackup->__construct();

// usage with all arguments
$result = $wireDatabaseBackup->__construct($path = '');
~~~~~

## Arguments

- `$path` (optional) `string` Path where database files are stored

## Exceptions

- `\Exception`
