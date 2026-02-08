# $wireMarkupRegions->prepend($selector, $content, $markup, array $options = array()): string

Source: `wire/core/WireMarkupRegions.php`

Prepend the region(s) that match the given $selector with the given $content markup

## Usage

~~~~~
// basic usage
$string = $wireMarkupRegions->prepend($selector, $content, $markup);

// usage with all arguments
$string = $wireMarkupRegions->prepend($selector, $content, $markup, array $options = array());
~~~~~

## Arguments

- `$selector` `string` See the update() method for details
- `$content` `string` Markup to prepend
- `$markup` `string` Document markup where region(s) exist
- `$options` (optional) `array` See the update() method for details

## Return value

- `string`
