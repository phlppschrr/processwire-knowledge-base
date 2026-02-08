# $selector->field($forceString = true): string|array|null

Source: `wire/core/Selector.php`

Get the field(s) of this Selector

Note that if calling this as a property (rather than a method) it can return either a string or an array.

## Arguments

- bool|int $forceString Specify one of the following: - `true` (bool): to only return a string, where multiple-fields will be split by pipe "|". (default) - `false` (bool): to return string if 1 field, or array of multiple fields (same behavior as field property). - `1` (int): to return only the first value (string).

## Return value

string|array|null

## See also

- [Selector::fields()](method-fields.md)

## Meta

- @since 3.0.42 Prior versions only supported the 'field' property.
