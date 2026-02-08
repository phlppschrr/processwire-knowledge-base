# WireDatabaseBackup::supportsExec()

Source: `wire/core/WireDatabaseBackup.php`

Determine if exec is available for the given command

Note that WireDatabaseBackup does not currently use exec() mode so this is here for future use.

@param array $options

@return bool

@throws \Exception on unknown exec type
