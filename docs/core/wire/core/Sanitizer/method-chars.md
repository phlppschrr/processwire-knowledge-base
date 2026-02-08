# Sanitizer::chars()

Source: `wire/core/Sanitizer.php`

Sanitize string value to have only the given characters

You must provide a string of allowed characters in the `$allow` argument. If not provided then
the only [ a-z A-Z 0-9 ] are allowed. You may optionally specify `[alpha]` to refer to any
ASCII alphabet character, or `[digit]` to refer to any digit.

~~~~~
echo $sanitizer->chars('foo123barBaz456', 'barz1'); // Outputs: 1baraz
echo $sanitizer->chars('(800) 555-1234', '[digit]', '.');  // Outputs: 800.555.1234
echo $sanitizer->chars('Decatur, GA 30030', '[alpha]', '-'); // Outputs: Decatur-GA
echo $sanitizer->chars('Decatur, GA 30030', '[alpha][digit]', '-'); // Outputs: Decatur-GA-30030
~~~~~


@param string $value Value to sanitize

@param string|array $allow Allowed characters string. If omitted then only alphanumeric [ a-z A-Z 0-9 ] are allowed.
 Use shortcut `[alpha]` to refer to any “a-z A-Z” char or `[digit]` to refer to any digit.

@param string $replacement Replace disallowed chars with this char or string, or omit for blank. (default='')

@param bool $collapse Collapse multiple $replacement chars to one and trim from return value? (default=true)

@param bool|null $mb Specify bool to force use of multibyte on or off, or omit to auto-detect. (default=null)

@return string

@since 3.0.126
