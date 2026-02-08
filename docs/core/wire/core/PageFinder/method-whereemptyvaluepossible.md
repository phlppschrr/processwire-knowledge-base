# $pageFinder->whereEmptyValuePossible(Field $field, $col, $selector, $query, $value, &$where): bool

Source: `wire/core/PageFinder.php`

Generate SQL and modify $query for situations where it should be possible to match empty values

This can include equals/not-equals with blank or 0, as well as greater/less-than searches that
can potentially match blank or 0.

## Arguments

- Field $field
- string $col
- Selector $selector
- DatabaseQuerySelect $query
- string $value The value presumed to be blank (passed the empty() test)
- string $where SQL where string that will be modified/appended

## Return value

bool Whether or not the query was handled and modified
