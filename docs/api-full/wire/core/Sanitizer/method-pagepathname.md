# $sanitizer->pagePathName($value, $beautify = false, $maxLength = 2048): string

Source: `wire/core/Sanitizer.php`

Sanitize a page path name

Returned path is not guaranteed to be valid or match a page, just sanitized.

## Usage

~~~~~
// basic usage
$string = $sanitizer->pagePathName($value);

// usage with all arguments
$string = $sanitizer->pagePathName($value, $beautify = false, $maxLength = 2048);
~~~~~

## Arguments

- `$value` `string` Value to sanitize
- `$beautify` (optional) `bool|int` Beautify the value? (default=false). Maybe any of the following: - `true` (bool): Beautify the individual page names in the path to remove redundant and trailing punctuation and more. - `false` (bool): Do not perform any conversion or attempt to make it more pretty, just sanitize (default). - `Sanitizer::translate` (constant): Translate UTF-8 characters to visually similar ASCII (using InputfieldPageName module settings). - `Sanitizer::toAscii` (constant): Convert UTF-8 characters to punycode ASCII. - `Sanitizer::toUTF8` (constant): Convert punycode ASCII to UTF-8. - `Sanitizer::okUTF8` (constant): Allow UTF-8 characters to appear in path (implied if $config->pageNameCharset is 'UTF8').
- `$maxLength` (optional) `int` Maximum length (default=2048)

## Return value

- `string` Sanitized path name
