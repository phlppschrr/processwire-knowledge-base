# $pagesNames->incrementName($name, $num = null): string

Source: `wire/core/PagesNames.php`

Increment the suffix of a page name, or add one if not present

## Usage

~~~~~
// basic usage
$string = $pagesNames->incrementName($name);

// usage with all arguments
$string = $pagesNames->incrementName($name, $num = null);
~~~~~

## Arguments

- `$name` `string`
- `$num` (optional) `int|null` Number to use, or omit to determine and increment automatically

## Return value

- `string`
