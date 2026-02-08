# $sanitizer->purifier(array $options = array()): MarkupHTMLPurifier

Source: `wire/core/Sanitizer.php`

Return a new HTML Purifier instance

See: [htmlpurifier.org](http://htmlpurifier.org)

## Usage

~~~~~
// basic usage
$markupHTMLPurifier = $sanitizer->purifier();

// usage with all arguments
$markupHTMLPurifier = $sanitizer->purifier(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` See [config options](http://htmlpurifier.org/live/configdoc/plain.html).

## Return value

- `MarkupHTMLPurifier`
