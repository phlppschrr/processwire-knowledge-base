# Paths::set()

Source: `wire/core/Paths.php`

Set a new path/URL location


@param string $key

@param mixed $value If the first character of the provided path is a slash, then that specific path will be used without modification.
	If the first character is anything other than a slash, then the 'root' variable will be prepended to the path.

@return Paths|WireData
