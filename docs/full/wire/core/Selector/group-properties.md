# Selector: properties

Source: `wire/core/Selector.php`

- `$not: bool` Is this a NOT selector? Indicates the selector returns the opposite if what it would otherwise.
- `$group: string|null` Group name for this selector (if field was prepended with a "group_name@").
- `$quote: string` Type of quotes value was in, or blank if it was not quoted. One of: '"[{(
- `$str: string` String value of selector, i.e. “a=b”.
- `$forceMatch: null|bool` When boolean, forces match (true) or force non-match (false). (default=null)
- `$altOperators: array` Alternate operators to use when primary fails match, supported only by compareTypeFind. Since 3.0.161 (default=[])
