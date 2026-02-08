# Sanitizer::path()

Source: `wire/core/Sanitizer.php`

Validate the given path, return path if valid, or false if not valid

Returns the given path if valid, or boolean false if not.

Path is validated per ProcessWire "name" convention of ascii only [-_./a-z0-9]
As a result, this function is primarily useful for validating ProcessWire paths,
and won't always work with paths outside ProcessWire.

This method validates only and does not sanitize. See `$sanitizer->pagePathName()` for a similar
method that does sanitiation.


@param string $value Path to validate

@param int|array $options Options to modify behavior, or maxLength (int) may be specified.
 - `allowDotDot` (bool): Whether to allow ".." in a path (default=false)
 - `maxLength` (int): Maximum length of allowed path (default=1024)

@return bool|string Returns false if invalid, actual path (string) if valid.

@see Sanitizer::pagePathName()
