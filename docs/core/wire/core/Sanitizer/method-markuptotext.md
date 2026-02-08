# Sanitizer::markupToText()

Source: `wire/core/Sanitizer.php`

Convert a string containing markup or entities to be plain text

This is one implementation but there is also a better one that you may prefer with the
`WireTextTools::markupToText()` method. Try both to determine which suits your needs
best:

~~~~~
$markup = '<html>a bunch of HTML here</html>';
// try both to see what you prefer:
$text1 = $sanitizer->markupToText($html);
$text2 = $sanitizer->getTextTools()->markupToText();
~~~~~


@param string $value String you want to convert

@param array $options Options to modify default behavior:
  - `newline` (string): Character(s) to replace newlines with (default="\n").
  - `separator` (string): Character(s) to separate HTML `<li>` items with (default="\n").
  - `entities` (bool): Entity encode returned value? (default=false).
  - `trim` (string): Character(s) to trim from beginning and end of value (default=" -,:;|\n\t").

@return string Converted string of text

@see WireTextTools::markupToText(), Sanitizer::markupToLine()
