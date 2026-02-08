# $paths->set($key, $value): Paths|WireData

Source: `wire/core/Paths.php`

Set a new path/URL location

## Arguments

- `$key` `string`
- `$value` `mixed` If the first character of the provided path is a slash, then that specific path will be used without modification. If the first character is anything other than a slash, then the 'root' variable will be prepended to the path.

## Return value

Paths|WireData
