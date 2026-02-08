# $pagesNames->adjustNameLength($name, $maxLength = 0): string

Source: `wire/core/PagesNames.php`

If name exceeds maxLength, truncate it, while keeping any numbered suffixes in place

## Usage

~~~~~
// basic usage
$string = $pagesNames->adjustNameLength($name);

// usage with all arguments
$string = $pagesNames->adjustNameLength($name, $maxLength = 0);
~~~~~

## Arguments

- `$name` `string`
- `$maxLength` (optional) `int`

## Return value

- `string`
