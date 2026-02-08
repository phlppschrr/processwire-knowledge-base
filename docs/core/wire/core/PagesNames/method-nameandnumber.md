# $pagesNames->nameAndNumber($name, $delimiter = ''): array

Source: `wire/core/PagesNames.php`

If given name has a numbered suffix, return array with name (excluding suffix) and the numbered suffix

Returns array like `[ 'name', 123 ]` where `name` is name without the suffix, and `123` is the numbered suffix.
If the name did not have a numbered suffix, then the 123 will be 0 and `name` will be the given `$name`.

## Usage

~~~~~
// basic usage
$array = $pagesNames->nameAndNumber($name);

// usage with all arguments
$array = $pagesNames->nameAndNumber($name, $delimiter = '');
~~~~~

## Arguments

- `$name` `string`
- `$delimiter` (optional) `string` Character(s) that separate name and numbered suffix

## Return value

- `array`
