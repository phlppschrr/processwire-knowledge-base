# $sanitizer->entities1($str, $flags = ENT_QUOTES, $encoding = 'UTF-8'): string

Source: `wire/core/Sanitizer.php`

Entity encode a string and don’t double encode it if already encoded

## Arguments

- `$str` `string` String to entity encode
- `$flags` (optional) `int|bool` See PHP htmlentities() function for flags.
- `$encoding` (optional) `string` Encoding of string (default="UTF-8").

## Return value

string Entity encoded string

## See also

- [Sanitizer::entities()](method-entities.md)
- [Sanitizer::unentities()](method-unentities.md)
