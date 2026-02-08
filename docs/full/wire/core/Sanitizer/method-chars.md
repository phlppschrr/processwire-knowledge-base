# $sanitizer->chars($value, $allow = '', $replacement = '', $collapse = true, $mb = null): string

Source: `wire/core/Sanitizer.php`

Sanitize string value to have only the given characters

You must provide a string of allowed characters in the `$allow` argument. If not provided then
the only [ a-z A-Z 0-9 ] are allowed. You may optionally specify `[alpha]` to refer to any
ASCII alphabet character, or `[digit]` to refer to any digit.

## Example

~~~~~
echo $sanitizer->chars('foo123barBaz456', 'barz1'); // Outputs: 1baraz
echo $sanitizer->chars('(800) 555-1234', '[digit]', '.');  // Outputs: 800.555.1234
echo $sanitizer->chars('Decatur, GA 30030', '[alpha]', '-'); // Outputs: Decatur-GA
echo $sanitizer->chars('Decatur, GA 30030', '[alpha][digit]', '-'); // Outputs: Decatur-GA-30030
~~~~~

## Usage

~~~~~
// basic usage
$string = $sanitizer->chars($value);

// usage with all arguments
$string = $sanitizer->chars($value, $allow = '', $replacement = '', $collapse = true, $mb = null);
~~~~~

## Arguments

- `$value` `string` Value to sanitize
- `$allow` (optional) `string|array` Allowed characters string. If omitted then only alphanumeric [ a-z A-Z 0-9 ] are allowed. Use shortcut `[alpha]` to refer to any “a-z A-Z” char or `[digit]` to refer to any digit.
- `$replacement` (optional) `string` Replace disallowed chars with this char or string, or omit for blank. (default='')
- `$collapse` (optional) `bool` Collapse multiple $replacement chars to one and trim from return value? (default=true)
- `$mb` (optional) `bool|null` Specify bool to force use of multibyte on or off, or omit to auto-detect. (default=null)

## Return value

- `string`

## Since

3.0.126
