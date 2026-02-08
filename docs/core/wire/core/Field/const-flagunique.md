# Field::flagUnique

Source: `wire/core/Field.php`

Field requires that the same value is not repeated more than once in its table 'data' column (when supported by Fieldtype)

When this flag is set and there is a non-empty $flagUnique property on the field, then it indicates a unique index
is currently present. When only this flag is present (no property), it indicates a request to remove the index and flag.
When only the property is present (no flag), it indicates a pending request to add unique index and flag.

@since 3.0.150
