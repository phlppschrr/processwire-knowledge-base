# $wireMarkupRegions->renderAttributes(array $attrs, $encode = true, $quote = '"'): string

Source: `wire/core/WireMarkupRegions.php`

Given an associative array of “key=value” attributes, render an HTML attribute string of them

- For boolean attributes without value (like "checked" or "selected") specify boolean true as the value.
- If value of any attribute is an array, it will be converted to a space-separated string.
- Values get entity encoded, unless you specify false for the second argument.

## Arguments

- array $attrs Associative array of attributes.
- bool $encode Entity encode attribute values? Default is true, so if they are already encoded, specify false.
- string $quote Quote style, specify double quotes, single quotes, or blank for none except when required (default=")

## Return value

string
