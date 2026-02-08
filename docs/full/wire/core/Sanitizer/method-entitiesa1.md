# $sanitizer->entitiesA1($value, $flags = ENT_QUOTES, $encoding = 'UTF-8'): array|string|int|float|bool

Source: `wire/core/Sanitizer.php`

Same as entitiesA() but does not double encode

## Usage

~~~~~
// basic usage
$array = $sanitizer->entitiesA1($value);

// usage with all arguments
$array = $sanitizer->entitiesA1($value, $flags = ENT_QUOTES, $encoding = 'UTF-8');
~~~~~

## Arguments

- `$value` `array|string|int|float|object|bool`
- `$flags` (optional) `int`
- `$encoding` (optional) `string`

## Return value

- `array|string|int|float|bool`

## See Also

- [Sanitizer::entitiesA()](method-entitiesa.md)
- [Sanitizer::entities1()](method-entities1.md)

## Since

3.0.194
