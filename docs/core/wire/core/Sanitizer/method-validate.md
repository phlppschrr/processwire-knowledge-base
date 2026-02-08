# $sanitizer->validate($value, $method = 'text', $fallback = null): null|mixed

Source: `wire/core/Sanitizer.php`

Validate that value remains unchanged by given sanitizer method, or return null if not

If change is just a type conversion change or surrounding whitespace (that gets trimmed)
then this is still considered valid.

Returns NULL or given $fallback value if value does not validate. Note that if results like
0, false or blank string are considered valid values, then this method can return them. So for
cases like that you should compare the return value with NULL (or whatever your $fallback is).

things like 0 or false (if that is a valid value) compare the return value with null before
assuming a value is not valid.

## Example

~~~~~
$sanitizer->validate('abc', 'alpha'); // valid: returns 'abc'
$sanitizer->validate('abc123', 'alpha'); invalid: returns null
~~~~~

## Usage

~~~~~
// basic usage
$sanitizer->validate($value);

// usage with all arguments
$sanitizer->validate($value, $method = 'text', $fallback = null);
~~~~~

## Arguments

- `$value` `string|int|array|float` Value to validate
- `$method` (optional) `string` Saniatizer method name or CSV names combo
- null|mixed mixed $fallback Optionally return this fallback value (rather than null) if value does not validate

## Return value

- `null|mixed` Returns sanitized value if it validates or null (or given fallback) if value does not validate

## Since

3.0.125
