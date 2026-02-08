# $sanitizer->trunc($str, $maxLength = 300, $options = array()): string

Source: `wire/core/Sanitizer.php`

Truncate string to given maximum length without breaking words and with no added visible extras

This is a shortcut to the truncate() sanitizer, sanitizing to nearest word with the `more` option
disabled and the `collapseLinesWith` set to 1 space (rather than ellipsis).

## Arguments

- string $str String to truncate
- int|array $maxLength Maximum allowed length in characters, or substitute $options argument here
- array $options See options for truncate() method or specify `type` option (word, punctuation, sentence, block).

## Return value

string

## Meta

- @since 3.0.157
