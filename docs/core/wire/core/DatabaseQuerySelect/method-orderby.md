# $databaseQuerySelect->orderby($value, $prepend = false): $this

Source: `wire/core/DatabaseQuerySelect.php`

Add an ORDER BY section to the query

## Arguments

- `$value` `string|array`
- `$prepend` (optional) `bool` Should the value be prepended onto the existing value? default is to append rather than prepend. Note that $prepend is applicable only when you pass this method a string. $prepend is ignored if you pass an array.

## Return value

$this
