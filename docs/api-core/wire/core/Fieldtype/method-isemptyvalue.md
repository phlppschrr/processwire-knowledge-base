# $fieldtype->isEmptyValue(Field $field, $value): bool

Source: `wire/core/Fieldtype.php`

Return whether the given value is considered empty or not.

This can be anything that might be present in a selector value and thus is
typically a string. However, it may be used outside of that purpose so you
shouldn't count on it being a string.

Example: an integer or text Fieldtype might not consider a "0" to be empty,
whereas a Page reference would.

This method is primarily used by the PageFinder::whereEmptyValuePossible()
method to determine whether to include non-present (null) rows.

3.0.164+: If given a Selector object for $value, PageFinder is proposing
handling the empty-value match condition internally rather than calling
the Fieldtype’s getMatchQuery() method. Return true if this Fieldtype would
prefer to handle the match, or false if not. Fieldtype modules do not need
to consider this unless they want to override the default empty value match
behavior in PageFinder::whereEmptyValuePossible().

## Usage

~~~~~
// basic usage
$bool = $fieldtype->isEmptyValue($field, $value);

// usage with all arguments
$bool = $fieldtype->isEmptyValue(Field $field, $value);
~~~~~

## Arguments

- `$field` `Field`
- `$value` `mixed`

## Return value

- `bool`
