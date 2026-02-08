# $wireMarkupRegions->after($selector, $content, $markup, array $options = array()): string

Source: `wire/core/WireMarkupRegions.php`

Insert the region(s) that match the given $selector after the given $content markup

## Usage

~~~~~
// basic usage
$string = $wireMarkupRegions->after($selector, $content, $markup);

// usage with all arguments
$string = $wireMarkupRegions->after($selector, $content, $markup, array $options = array());
~~~~~

## Arguments

- `$selector` `string` See the update() method for details
- `$content` `string` Markup to prepend
- `$markup` `string` Document markup where region(s) exist
- `$options` (optional) `array` See the update() method for details

## Return value

- `string`
