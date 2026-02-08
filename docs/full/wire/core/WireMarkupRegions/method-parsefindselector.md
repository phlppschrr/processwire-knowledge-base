# $wireMarkupRegions->parseFindSelector($find): array

Source: `wire/core/WireMarkupRegions.php`

Given a $find selector return array with tests and other meta info

## Usage

~~~~~
// basic usage
$array = $wireMarkupRegions->parseFindSelector($find);
~~~~~

## Arguments

- `$find` `string`

## Return value

- `array` Returns array of [ 'tests' => [ 0 => '', 1 => '', ...], 'find' => '', 'findTag' => '', 'hasClass' => '', ]
