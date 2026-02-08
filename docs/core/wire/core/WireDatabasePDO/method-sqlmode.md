# WireDatabasePDO::sqlMode()

Source: `wire/core/WireDatabasePDO.php`

Get SQL mode, set SQL mode, add to existing SQL mode, or remove from existing SQL mode


~~~~~
// Get SQL mode
$mode = $database->sqlMode();

// Add an SQL mode
$database->sqlMode('add', 'STRICT_TRANS_TABLES');

// Remove SQL mode if version at least 5.7.0
$database->sqlMode('remove', 'ONLY_FULL_GROUP_BY', '5.7.0');
~~~~~

@param string $action Specify "get", "set", "add" or "remove". (default="get")

@param string $mode Mode string or CSV string with SQL mode(s), i.e. "STRICT_TRANS_TABLES,ONLY_FULL_GROUP_BY".
  This argument should be omitted when using the "get" action.

@param string $minVersion Make the given action only apply if MySQL version is at least $minVersion, i.e. "5.7.0".

@param \PDO PDO connection to use or omit for current (default=null) 3.0.175+

@return string|bool Returns string in "get" action, boolean false if required version not present, or true otherwise.

@throws WireException If given an invalid $action
