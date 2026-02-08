# $wireFileTools->chmod($path, $recursive = false, $chmod = null): bool

Source: `wire/core/WireFileTools.php`

Change the read/write mode of a file or directory, consistent with ProcessWire's configuration settings

Unless a specific mode is provided via the `$chmod` argument, this method uses the `$config->chmodDir`
and `$config->chmodFile` settings in /site/config.php.

This method also provides the option of going recursive, adjusting the read/write mode for an entire
file/directory tree at once.

The `$recursive` or `$chmod` arguments may be optionally swapped in order (since 3.0.34).

~~~~~
// Update the mode of /site/assets/cache/foo-bar/ recursively
$files->chmod($config->paths->cache . 'foo-bar/', true);
~~~~~

## Arguments

- string $path Path or file that you want to adjust mode for (may be a path/directory or a filename).
- bool|string $recursive If set to true, all files and directories in $path will be recursively set as well (default=false).
- string|null|bool $chmod If you want to set the mode to something other than ProcessWire's chmodFile/chmodDir settings, you may override it by specifying it here. Ignored otherwise. Format should be a string, like "0755".

## Return value

bool Returns true if all changes were successful, or false if at least one chmod failed.

## Throws

- WireException when it receives incorrect chmod format
