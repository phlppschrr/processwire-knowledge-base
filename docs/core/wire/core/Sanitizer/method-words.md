# $sanitizer->words($value, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Given string return a new string containing only words

## Usage

~~~~~
// basic usage
$string = $sanitizer->words($value);

// usage with all arguments
$string = $sanitizer->words($value, array $options = array());
~~~~~

## Arguments

- $value
- `$options` (optional) `array` - `separator` (string): String to use to separate words (default=' ') - `ascii` (string): Only allow ASCII characters in words? (default=false) - `keepUnderscore` (bool): Keep underscores as part of words? (default=false) - `keepHyphen` (bool): Keep hyphenated words? (default=false) - `keepChars` (array): Additional non word characters to keep (default=[]) - `maxWordLength` (int): Maximum word length (default=80) - `minWordLength` (int): Minimum word length (default=1) - `maxLength` (int): Maximum return value length (default=1024) - `beautify` (bool): Make ugly strings more pretty? This collapses and trims redundant separators (default=true)

## Return value

- `string`

## Since

3.0.195
