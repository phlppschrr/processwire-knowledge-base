# $wireMarkupRegions->append($selector, $content, $markup, array $options = array()): string

Source: `wire/core/WireMarkupRegions.php`

Append the region(s) that match the given $selector with the given $content markup

## Usage

~~~~~
// basic usage
$string = $wireMarkupRegions->append($selector, $content, $markup);

// usage with all arguments
$string = $wireMarkupRegions->append($selector, $content, $markup, array $options = array());
~~~~~

## Arguments

- `$selector` `string` See the update() method $selector argument for details
- `$content` `string` Markup to append
- `$markup` `string` Document markup where region(s) exist
- `$options` (optional) `array` See the update() method $options argument for details

## Return value

- `string`
