# Sanitizer::word()

Source: `wire/core/Sanitizer.php`

Return first word in given string


@param string $value String containing one or more words

@param array $options Options to adjust behavior:
 - `keepNumbers` (bool): Allow numbers as return value? (default=true)
 - `keepNumberFormat` (bool): Keep minus/comma/period in numbers rather than splitting into words? Also requires keepNumbers==true. (default=false)
 - `keepUnderscore` (bool): Keep underscores as part of words? (default=false)
 - `keepHyphen` (bool): Keep hyphenated words? (default=false)
 - `keepChars` (array): Specify any of these to also keep as part of words ['.', ',', ';', '/', '*', ':', '+', '<', '>', '_', '-' ] (default=[])
 - `minWordLength` (int): Minimum word length (default=1)
 - `maxWordLength` (int): Maximum word length (default=80)
 - `maxWords` (int): Maximum words (default=1 or 99 if a seperator option is specified)
 - `maxLength` (int): Maximum returned string length (default=1024)
 - `stripTags` (bool): Strip markup tags so they don’t contribute to returned word? (default=true)
 - `separator' (string): Merge multiple words into one word split by this character? (default='', disabled) 3.0.195+
 - `ascii` (bool): Allow only ASCII word characters? (default=false)
 - `beautify` (bool): Make ugly strings more pretty? This collapses and trims redundant separators (default=false)

@return string

@see Sanitizer::wordsArray()

@since 3.0.162
