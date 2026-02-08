# Functions::wireChmod()

Source: `wire/core/Functions.php`

Change the mode of a file or directory (optionally recursive)

If no `$chmod` mode argument is specified the `$config->chmodFile` or $config->chmodDir` settings will be used.

This is procedural version of the `$files->chmod()` method.


@param string $path May be a directory or a filename

@param bool $recursive If set to true, all files and directories in $path will be recursively set as well.

@param string $chmod If you want to set the mode to something other than PW's chmodFile/chmodDir settings,
  you may override it by specifying it here. Ignored otherwise. Format should be a string, like "0755".

@return bool Returns true if all changes were successful, or false if at least one chmod failed.

@throws WireException when it receives incorrect chmod format

@see WireFileTools::chmod()
