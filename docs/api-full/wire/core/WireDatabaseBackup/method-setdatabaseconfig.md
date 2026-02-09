# $wireDatabaseBackup->setDatabaseConfig($config): $this

Source: `wire/core/WireDatabaseBackup.php`

Set the database configuration information

## Usage

~~~~~
// basic usage
$result = $wireDatabaseBackup->setDatabaseConfig($config);
~~~~~

## Arguments

- `$config` (optional) `array|Config|object` Containing these properties: - dbUser - dbHost - dbPort - dbName - dbPass - dbPath (optional) - dbCharset (optional)

## Return value

- `$this`

## Exceptions

- `\Exception` if missing required config settings
