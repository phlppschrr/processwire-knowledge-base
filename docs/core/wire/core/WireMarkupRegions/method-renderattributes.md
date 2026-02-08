# $wireMarkupRegions->renderAttributes(array $attrs, $encode = true, $quote = '"'): string

Source: `wire/core/WireMarkupRegions.php`

Given an associative array of “key=value” attributes, render an HTML attribute string of them

- For boolean attributes without value (like "checked" or "selected") specify boolean true as the value.
- If value of any attribute is an array, it will be converted to a space-separated string.
- Values get entity encoded, unless you specify false for the second argument.

## Usage

~~~~~
// basic usage
$string = $wireMarkupRegions->renderAttributes($attrs);

// usage with all arguments
$string = $wireMarkupRegions->renderAttributes(array $attrs, $encode = true, $quote = '"');
~~~~~

## Arguments

- `$attrs` `array` Associative array of attributes.
- `$encode` (optional) `bool` Entity encode attribute values? Default is true, so if they are already encoded, specify false.
- `$quote` (optional) `string` Quote style, specify double quotes, single quotes, or blank for none except when required (default=")

## Return value

- `string`
