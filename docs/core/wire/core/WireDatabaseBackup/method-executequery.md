# WireDatabaseBackup::executeQuery()

Source: `wire/core/WireDatabaseBackup.php`

Execute an SQL query, either a string or PDOStatement

@param string|\PDOStatement $query

@param bool|array $options May be boolean (for haltOnError), or array containing the property (i.e. $options array)
 - `haltOnError` (bool): Halt execution when error occurs? (default=false)

@return bool Query result

@throws \Exception if haltOnError, otherwise it populates $this->errors
