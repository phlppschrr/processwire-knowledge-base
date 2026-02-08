# $sanitizer->entities1($str, $flags = ENT_QUOTES, $encoding = 'UTF-8'): string

Source: `wire/core/Sanitizer.php`

Entity encode a string and don’t double encode it if already encoded

## Arguments

- string $str String to entity encode
- int|bool $flags See PHP htmlentities() function for flags.
- string $encoding Encoding of string (default="UTF-8").

## Return value

string Entity encoded string

## See also

- [Sanitizer::entities()](method-entities.md)
- [Sanitizer::unentities()](method-unentities.md)
