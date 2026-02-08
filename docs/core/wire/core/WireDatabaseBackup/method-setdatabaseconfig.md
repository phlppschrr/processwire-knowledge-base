# $wireDatabaseBackup->setDatabaseConfig($config): $this

Source: `wire/core/WireDatabaseBackup.php`

Set the database configuration information

## Arguments

- array|Config|object $config Containing these properties: - dbUser - dbHost - dbPort - dbName - dbPass - dbPath (optional) - dbCharset (optional)

## Return value

$this

## Throws

- \Exception if missing required config settings
