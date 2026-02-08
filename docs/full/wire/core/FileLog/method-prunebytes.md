# FileLog::pruneBytes()

Source: `wire/core/FileLog.php`

Prune log file to specified number of bytes (from the end)

@param int $bytes

@return int|bool positive integer on success, 0 if no prune necessary, or boolean false on failure.
