# $databaseQuerySelectFulltext->match($tableName, $fieldName, $operator, $value): $this

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Update the query (provided to the constructor) to match the given arguments

## Arguments

- string $tableName
- string $fieldName
- string $operator
- string|int|array $value Value to match. Array value support added 3.0.141 (not used by PageFinder)

## Return value

$this

## Throws

- WireException If given $operator argument is not implemented here
