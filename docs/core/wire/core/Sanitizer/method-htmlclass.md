# $sanitizer->htmlClass($value): string

Source: `wire/core/Sanitizer.php`

Sanitize string to ASCII-only HTML class attribute value

Note that this does not support all possible characters in an HTML class attribute
and instead focuses on the most commonly used ones. Characters allowed in HTML class
attributes from this method include: `-_:@a-zA-Z0-9`. This method does not allow
values that have no letters or digits.

## Arguments

- `$value` `string`

## Return value

string

## Since

3.0.212
