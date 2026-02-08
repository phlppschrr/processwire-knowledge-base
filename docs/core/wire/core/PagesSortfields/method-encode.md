# $pagesSortfields->encode($sortfield, $default = 'sort'): string|int

Source: `wire/core/PagesSortfields.php`

Encodes a sortfield from a fieldname to a signed integer (ID) representing a custom field, or native field name

The returned value will be a negative value (or string preceded by a dash) if the sortfield is reversed.

## Arguments

- `$sortfield` `string`
- `$default` (optional) `string` Default sortfield name (default='sort')

## Return value

string|int
