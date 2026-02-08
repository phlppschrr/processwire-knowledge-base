# Sanitizer::wordsArray()

Source: `wire/core/Sanitizer.php`

Return array of all words in given value (excluding punctuation and other non-word characters)


@param string|array $value String containing words

@param array $options
 - `keepNumbers` (bool): Keep number-only words in return value? (default=true)
 - `keepNumberFormat` (bool): Keep minus/comma/period in numbers rather than splitting into words? Also requires keepNumbers==true. (default=false)
 - `keepUnderscore` (bool): Keep underscores as part of words? (default=false)
 - `keepHyphen` (bool): Keep hyphenated words? (default=false)
 - `keepApostrophe` (bool): Keep apostrophe as part of words? (default=true) 3.0.168+
 - `keepChars` (array): Specify any of these to also keep as part of words ['.', ',', ';', '/', '*', ':', '+', '<', '>', '_', '-' ] (default=[])
 - `minWordLength` (int): Minimum word length (default=1)
 - `maxWordLength` (int): Maximum word length (default=80)
 - `maxWords` (int): Maximum number of words allowed (default=0, no limit)
 - `stripTags` (bool): Strip markup tags so they don’t contribute to returned word list? (default=true)
 - `truncate` (bool): Truncate rather than remove words that exceed maxWordLength? (default=false) 3.0.250+

@return array

@since 3.0.160
