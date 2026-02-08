# PagefilesManager::emptyPath()

Source: `wire/core/PagefilesManager.php`

Empty out the published files (delete all of them)


@param bool $rmdir Remove the directory too? (default=false)

@param bool $recursive Recursively do the same for subdirectories? (default=true)

@return bool True on success, false on error (since 3.0.17, previous versions had no return value).
