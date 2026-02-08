# $functions->wireChmod($path, $recursive = false, $chmod = null): bool

Source: `wire/core/Functions.php`

Change the mode of a file or directory (optionally recursive)

If no `$chmod` mode argument is specified the `$config->chmodFile` or $config->chmodDir` settings will be used.

This is procedural version of the `$files->chmod()` method.

## Arguments

- `$path` `string` May be a directory or a filename
- `$recursive` (optional) `bool` If set to true, all files and directories in $path will be recursively set as well.
- `$chmod` (optional) `string` If you want to set the mode to something other than PW's chmodFile/chmodDir settings, you may override it by specifying it here. Ignored otherwise. Format should be a string, like "0755".

## Return value

bool Returns true if all changes were successful, or false if at least one chmod failed.

## Throws

- WireException when it receives incorrect chmod format

## See also

- [WireFileTools::chmod()](../WireFileTools/method-chmod.md)
