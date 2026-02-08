# $selectors->getSelectorByFieldValue($fieldName, $value, $or = false, $all = false): Selector|array|null

Source: `wire/core/Selectors.php`

Get the first selector that uses given field name AND has the given value

Using **$or:** By default this excludes selectors that have fields or values in an OR expression, like "a|b|c".
So if you specified field "a" it would not be matched. If you wanted it to still match, specify true
for the $or argument.

Using **$all:** By default only the first matching selector is returned. If you want it to return all
matching selectors in an array, then specify true for the $all argument. This changes the return value
to always be an array of Selector objects, or a blank array if no match.

## Usage

~~~~~
// basic usage
$selector = $selectors->getSelectorByFieldValue($fieldName, $value);

// usage with all arguments
$selector = $selectors->getSelectorByFieldValue($fieldName, $value, $or = false, $all = false);
~~~~~

## Arguments

- `$fieldName` `string` Name of field to match
- `$value` `string|int` Value that must match
- `$or` (optional) `bool` Allow fields and values that appear in OR expressions? (default=false)
- `$all` (optional) `bool` Return an array of all matching Selector objects? (default=false)

## Return value

- `Selector|array|null` Returns null if field not present in selectors (or blank array if $all mode)

## Since

3.0.142
