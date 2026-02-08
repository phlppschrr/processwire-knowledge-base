# $sanitizer->unentities($str, $flags = ENT_QUOTES, $encoding = 'UTF-8'): string

Source: `wire/core/Sanitizer.php`

Remove entity encoded characters from a string.

Wrapper for PHP's `html_entity_decode()` function that contains typical ProcessWire usage defaults.

The arguments used here are identical to those for PHP’s (except `$flags` can be boolean true):
[html_entity_decode](http://www.php.net/manual/en/function.html-entity-decode.php) function.

For the `$flags` argument, specify boolean `true` if you want to perform a more comprehensive entity
decode than what PHP does. That will make it convert all UTF-8 entities (including decimal and hex numbered
entities), and it will remove any remaining entity sequences if the could not be converted, ensuring there
are no entities possible in returned value.

## Usage

~~~~~
// basic usage
$string = $sanitizer->unentities($str);

// usage with all arguments
$string = $sanitizer->unentities($str, $flags = ENT_QUOTES, $encoding = 'UTF-8');
~~~~~

## Arguments

- `$str` `string` String to remove entities from
- `$flags` (optional) `int|bool` See PHP html_entity_decode function for flags, OR specify boolean true to convert all entities and remove any that cannot be converted (since 3.0.105).
- `$encoding` (optional) `string` Encoding (default="UTF-8").

## Return value

- `string` String with entities removed.

## See Also

- [Sanitizer::entities()](method-entities.md)
