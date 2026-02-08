# $wireMarkupRegions->remove($selector, $markup, array $options = array()): string

Source: `wire/core/WireMarkupRegions.php`

Remove the region(s) that match the given $selector

## Usage

~~~~~
// basic usage
$string = $wireMarkupRegions->remove($selector, $markup);

// usage with all arguments
$string = $wireMarkupRegions->remove($selector, $markup, array $options = array());
~~~~~

## Arguments

- `$selector` `string` See the update() method for details
- `$markup` `string` Document markup where region(s) exist
- `$options` (optional) `array` See the update() method for details

## Return value

- `string`
