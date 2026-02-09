# $wireMarkupRegions->findMulti($selector, $markup, array $options = array()): array

Source: `wire/core/WireMarkupRegions.php`

Multi-selector version of find(), where $selector contains CSV

## Usage

~~~~~
// basic usage
$array = $wireMarkupRegions->findMulti($selector, $markup);

// usage with all arguments
$array = $wireMarkupRegions->findMulti($selector, $markup, array $options = array());
~~~~~

## Arguments

- `$selector` `string`
- `$markup` `string`
- `$options` (optional) `array`

## Return value

- `array`
