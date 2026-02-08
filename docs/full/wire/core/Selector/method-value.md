# $selector->value($forceString = true): string|array|null

Source: `wire/core/Selector.php`

Get the value(s) of this Selector

Note that if calling this as a property (rather than a method) it can return either a string or an array.

## Usage

~~~~~
// basic usage
$string = $selector->value();

// usage with all arguments
$string = $selector->value($forceString = true);
~~~~~

## Arguments

- `$forceString` (optional) `bool|int` Specify one of the following: - `true` (bool): to only return a string, where multiple-values will be split by pipe "|". (default) - `false` (bool): to return string if 1 value, or array of multiple values (same behavior as value property). - `1` (int): to return only the first value (string).

## Return value

- `string|array|null`

## See Also

- [Selector::values()](method-values.md)

## Since

3.0.42 Prior versions only supported the 'value' property.
