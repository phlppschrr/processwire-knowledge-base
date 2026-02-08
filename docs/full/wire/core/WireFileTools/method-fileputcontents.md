# WireFileTools::filePutContents()

Source: `wire/core/WireFileTools.php`

Create (overwrite or append) a file, put the $contents in it, and adjust permissions

This is the same as PHP’s `file_put_contents()` except that it’s preferable to use this in
ProcessWire because it adjusts the file permissions configured with `$config->chmodFile`.


@param string $filename Filename to write to

@param string|mixed $contents Contents to write to file

@param int $flags Flags to modify behavior:
 - `FILE_APPEND` (constant): Append to file if it already exists.
 - `LOCK_EX` (constant): Acquire exclusive lock to file while writing.

@return int|bool Number of bytes written or boolean false on fail

@throws WireException if given invalid $filename (since 3.0.118)

@see WireFileTools::fileGetContents()
