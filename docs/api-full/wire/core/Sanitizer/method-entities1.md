# $sanitizer->entities1($str, $flags = ENT_QUOTES, $encoding = 'UTF-8'): string

Source: `wire/core/Sanitizer.php`

Entity encode a string and don’t double encode it if already encoded

## Usage

~~~~~
// basic usage
$string = $sanitizer->entities1($str);

// usage with all arguments
$string = $sanitizer->entities1($str, $flags = ENT_QUOTES, $encoding = 'UTF-8');
~~~~~

## Arguments

- `$str` `string` String to entity encode
- `$flags` (optional) `int|bool` See PHP htmlentities() function for flags.
- `$encoding` (optional) `string` Encoding of string (default="UTF-8").

## Return value

- `string` Entity encoded string

## See Also

- [Sanitizer::entities()](method-entities.md)
- [Sanitizer::unentities()](method-unentities.md)
