# $pagesRawFinder->flattenValues(array $values, $prefix = '', $delimiter = '.'): array

Source: `wire/core/PagesRaw.php`

Flatten multidimensional values from array['a']['b']['c'] to array['a.b.c']

## Usage

~~~~~
// basic usage
$array = $pagesRawFinder->flattenValues($values);

// usage with all arguments
$array = $pagesRawFinder->flattenValues(array $values, $prefix = '', $delimiter = '.');
~~~~~

## Arguments

- `$values` `array`
- `$prefix` (optional) `string` Prefix for recursive use
- `$delimiter` (optional) `string`

## Return value

- `array`

## Since

3.0.193
