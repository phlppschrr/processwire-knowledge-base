# $wireSaveableItems->error($text, $flags = 0): Wire|WireSaveableItems

Source: `wire/core/WireSaveableItems.php`

Record an error

## Usage

~~~~~
// basic usage
$wire = $wireSaveableItems->error($text);

// usage with all arguments
$wire = $wireSaveableItems->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string`
- `$flags` (optional) `int|bool` See Notices::flags

## Return value

- `Wire|WireSaveableItems`
