# $sanitizer->markupToText($value, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Convert a string containing markup or entities to be plain text

This is one implementation but there is also a better one that you may prefer with the
`WireTextTools::markupToText()` method. Try both to determine which suits your needs
best:

## Example

~~~~~
$markup = '<html>a bunch of HTML here</html>';
// try both to see what you prefer:
$text1 = $sanitizer->markupToText($html);
$text2 = $sanitizer->getTextTools()->markupToText();
~~~~~

## Usage

~~~~~
// basic usage
$string = $sanitizer->markupToText($value);

// usage with all arguments
$string = $sanitizer->markupToText($value, array $options = array());
~~~~~

## Arguments

- `$value` `string` String you want to convert
- `$options` (optional) `array` Options to modify default behavior: - `newline` (string): Character(s) to replace newlines with (default="\n"). - `separator` (string): Character(s) to separate HTML `<li>` items with (default="\n"). - `entities` (bool): Entity encode returned value? (default=false). - `trim` (string): Character(s) to trim from beginning and end of value (default=" -,:;|\n\t").

## Return value

- `string` Converted string of text

## See Also

- [WireTextTools::markupToText()](../WireTextTools/method-markuptotext.md)
- [Sanitizer::markupToLine()](method-markuptoline.md)
