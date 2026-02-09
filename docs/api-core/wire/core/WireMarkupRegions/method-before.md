# $wireMarkupRegions->before($selector, $content, $markup, array $options = array()): string

Source: `wire/core/WireMarkupRegions.php`

Insert region(s) that match the given $selector before the given $content markup

## Usage

~~~~~
// basic usage
$string = $wireMarkupRegions->before($selector, $content, $markup);

// usage with all arguments
$string = $wireMarkupRegions->before($selector, $content, $markup, array $options = array());
~~~~~

## Arguments

- `$selector` `string` See the update() method for details
- `$content` `string` Markup to prepend
- `$markup` `string` Document markup where region(s) exist
- `$options` (optional) `array` See the update() method for details

## Return value

- `string`
