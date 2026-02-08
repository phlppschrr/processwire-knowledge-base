# $wireFileTools->filePutContents($filename, $contents, $flags = 0): int|bool

Source: `wire/core/WireFileTools.php`

Create (overwrite or append) a file, put the $contents in it, and adjust permissions

This is the same as PHP’s `file_put_contents()` except that it’s preferable to use this in
ProcessWire because it adjusts the file permissions configured with `$config->chmodFile`.

## Arguments

- `$filename` `string` Filename to write to
- `$contents` `string|mixed` Contents to write to file
- `$flags` (optional) `int` Flags to modify behavior: - `FILE_APPEND` (constant): Append to file if it already exists. - `LOCK_EX` (constant): Acquire exclusive lock to file while writing.

## Return value

int|bool Number of bytes written or boolean false on fail

## Throws

- WireException if given invalid $filename (since 3.0.118)

## See also

- [WireFileTools::fileGetContents()](method-filegetcontents.md)
