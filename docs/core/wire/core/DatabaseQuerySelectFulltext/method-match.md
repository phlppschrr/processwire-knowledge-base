# $databaseQuerySelectFulltext->match($tableName, $fieldName, $operator, $value): $this

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Update the query (provided to the constructor) to match the given arguments

## Usage

~~~~~
// basic usage
$result = $databaseQuerySelectFulltext->match($tableName, $fieldName, $operator, $value);
~~~~~

## Arguments

- `$tableName` `string`
- `$fieldName` `string`
- `$operator` `string`
- `$value` `string|int|array` Value to match. Array value support added 3.0.141 (not used by PageFinder)

## Return value

- `$this`

## Exceptions

- `WireException` If given $operator argument is not implemented here
