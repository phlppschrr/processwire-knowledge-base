# $sanitizer->minLength($value, $minLength = 1, $padChar = '', $padLeft = false): string

Source: `wire/core/Sanitizer.php`

Validate or sanitize a string to have a minimum length

If string meets minimum length it is returned as-is.

Note that the default behavior of this function is to validate rather than sanitize the value.
Meaning, it will return blank if the string does not meet the minimum length. Specify the `$padChar`
argument to change that behavior.

If string does not meet minimum length, blank will be returned, unless a `$padChar` is defined in which
case the string will be padded with as many copies of that $padChar are necessary to meet the minimum
length. By default it padds to the right, but you can specify `true` for the `$padLeft` argument to
make it pad to the left instead.

~~~~~~
$value = $sanitizer->minLength('foo'); // returns "foo"
$value = $sanitizer->minLength('foo', 3); // returns "foo"
$value = $sanitizer->minLength('foo', 5); // returns blank string
$value = $sanitizer->minLength('foo', 5, 'o'); // returns "foooo"
$value = $sanitizer->minLength('foo', 5, 'o', true); // returns "oofoo"
~~~~~~

## Arguments

- string $value Value to enforcer a minimum length for
- int $minLength Minimum allowed length
- string $padChar Pad string with this character if it does not meet minimum length (default='')
- bool $padLeft Pad to left rather than right? (default=false)

## Return value

string

## See also

- [Sanitizer::maxLength()](method-maxlength.md)
