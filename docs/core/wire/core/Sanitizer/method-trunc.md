# Sanitizer::trunc()

Source: `wire/core/Sanitizer.php`

Truncate string to given maximum length without breaking words and with no added visible extras

This is a shortcut to the truncate() sanitizer, sanitizing to nearest word with the `more` option
disabled and the `collapseLinesWith` set to 1 space (rather than ellipsis).


@param string $str String to truncate

@param int|array $maxLength Maximum allowed length in characters, or substitute $options argument here

@param array $options See options for truncate() method or specify `type` option (word, punctuation, sentence, block).

@return string

@since 3.0.157
