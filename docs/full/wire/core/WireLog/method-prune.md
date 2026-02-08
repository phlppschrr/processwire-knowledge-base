# WireLog::prune()

Source: `wire/core/WireLog.php`

Prune log file to contain only entries from last [n] days


@param string $name Name of log file, excluding path and extension.

@param int $days Number of days

@return int Number of items in newly pruned log file or boolean false on failure

@throws WireException
