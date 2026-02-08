# $sanitizer->trunc($str, $maxLength = 300, $options = array()): string

Source: `wire/core/Sanitizer.php`

Truncate string to given maximum length without breaking words and with no added visible extras

This is a shortcut to the truncate() sanitizer, sanitizing to nearest word with the `more` option
disabled and the `collapseLinesWith` set to 1 space (rather than ellipsis).

## Usage

~~~~~
// basic usage
$string = $sanitizer->trunc($str);

// usage with all arguments
$string = $sanitizer->trunc($str, $maxLength = 300, $options = array());
~~~~~

## Arguments

- `$str` `string` String to truncate
- `$maxLength` (optional) `int|array` Maximum allowed length in characters, or substitute $options argument here
- `$options` (optional) `array` See options for truncate() method or specify `type` option (word, punctuation, sentence, block).

## Return value

- `string`

## Since

3.0.157
