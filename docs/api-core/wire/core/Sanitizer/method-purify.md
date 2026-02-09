# $sanitizer->purify($str, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Purify HTML markup using HTML Purifier

See: [htmlpurifier.org](http://htmlpurifier.org)

## Usage

~~~~~
// basic usage
$string = $sanitizer->purify($str);

// usage with all arguments
$string = $sanitizer->purify($str, array $options = array());
~~~~~

## Arguments

- `$str` `string` String to purify
- `$options` (optional) `array` See [config options](http://htmlpurifier.org/live/configdoc/plain.html).

## Return value

- `string` Purified markup string.
