# WireTempDir::removeExpiredDirs()

Source: `wire/core/WireTempDir.php`

Remove expired directories in the given $path

Also removes $path if it's found that everything in it is expired.

@param string $path

@param int Max age in seconds

@return bool
