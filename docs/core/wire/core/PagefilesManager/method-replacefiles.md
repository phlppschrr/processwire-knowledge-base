# PagefilesManager::replaceFiles()

Source: `wire/core/PagefilesManager.php`

Replace all page’s files with those from given path


@param string $fromPath

@param bool $move Move files to destination rather than copy? (default=false)

@return int Number of files/directories copied.

@throws WireException if given a path that does not exist.

@since 3.0.114
