# $pageFinder->whereEmptyValuePossible(Field $field, $col, $selector, $query, $value, &$where): bool

Source: `wire/core/PageFinder.php`

Generate SQL and modify $query for situations where it should be possible to match empty values

This can include equals/not-equals with blank or 0, as well as greater/less-than searches that
can potentially match blank or 0.

## Usage

~~~~~
// basic usage
$bool = $pageFinder->whereEmptyValuePossible($field, $col, $selector, $query, $value, $where);

// usage with all arguments
$bool = $pageFinder->whereEmptyValuePossible(Field $field, $col, $selector, $query, $value, &$where);
~~~~~

## Arguments

- `$field` `Field`
- `$col` `string`
- `$selector` `Selector`
- `$query` `DatabaseQuerySelect`
- `$value` `string` The value presumed to be blank (passed the empty() test)
- `$where` `string` SQL where string that will be modified/appended

## Return value

- `bool` Whether or not the query was handled and modified
