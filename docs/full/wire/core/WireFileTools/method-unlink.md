# WireFileTools::unlink()

Source: `wire/core/WireFileTools.php`

Unlink/delete file with additional protections relative to PHP unlink()

- This method requires a full pathname to a file to unlink and does not
  accept any kind of relative path traversal.

- This method will be limited to unlink files only in /site/assets/ if you
  specify `true` for the `$limitPath` option (recommended).


@param string $filename

@param string|bool $limitPath Limit only to files within some starting path? (default=false)
 - Boolean true to limit unlink operations to somewhere within /site/assets/ (only known always writable path).
 - Boolean false to disable to security feature. (default)
 - An alternative path (string) that represents the starting path (full disk path) to limit deletions to.
 - An array with multiple of the above string option.

@param bool $throw Throw exception on error?

@return bool True on success, false on fail

@throws WireException If file is not allowed to be removed or unlink fails

@since 3.0.118
