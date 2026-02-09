# $sanitizer->selectorValue($value, $options = array()): string|int|bool|mixed

Source: `wire/core/Sanitizer.php`

Sanitizes a string value that needs to go in a ProcessWire selector

Always use this to sanitize any string values you are inserting in selector strings.
This ensures that the value can't be confused for another component of the selector string.
This method may remove characters, escape characters, or surround the string in quotes.

## Example

~~~~~
// Sanitize text for a search on title and body fields
$q = $input->get->text('q'); // text search query
$results = $pages->find("title|body%=" . $sanitizer->selectorValue($q));

// In 3.0.127 you can also provide an array for the $value argument
$val = $sanitizer->selectorValue([ 'foo', 'bar', 'baz' ]);
echo $val; // outputs: foo|bar|baz
~~~~~

## Usage

~~~~~
// basic usage
$string = $sanitizer->selectorValue($value);

// usage with all arguments
$string = $sanitizer->selectorValue($value, $options = array());
~~~~~

## Arguments

- `$value` `string|array` String value to sanitize (assumed to be UTF-8), or in 3.0.127+ you may use an array and it will be sanitized to an OR value string.
- `$options` (optional) `array|int` Options to modify behavior. Note version 1 supports only `maxLength` and `useQuotes` options. - `version` (int): Version 1 or 2 (default=2). Version 2 available in 3.0.156+. Note option is remembered between calls. - `maxLength` (int): Maximum number of allowed characters (default=100). This may also be specified instead of $options array. - `useQuotes` (bool): Allow selectorValue() function to add quotes if it deems them necessary? (default=true) - All following options are only supported in version 2 (available in 3.0.156+): - `allowArray` (bool): Allow arrays to convert to OR-strings? If false, only 1st item in arrays is used. (default=true) - `allowSpace` (bool): Allow spaces? False to remove or true to allow (default=true) 3.0.168+ - `operator` (string): Operator being used in selector, optionally apply for operator-specific filtering. - `emptyValue` (string): Value to return if selector reduced to blank. Optionally use this to return something that could never match, or return something for you to evaluate yourself, like boolean false. (default=blank string) - `blacklist` (array): Additional characters you want to disallow. (default=[]) - `whitelist` (array): Characters that are in default blacklist that you still want to allow. (default=[]) - `quotelist` (array): Additional characters that should always trigger quoted value. (default=[]) - If an integer is specified for $options, it is assumed to be the maxLength value.

## Return value

- `string|int|bool|mixed` Value ready to be used as the value component in a selector string. Always returns string unless you specify something different for 'emptyValue' option.
