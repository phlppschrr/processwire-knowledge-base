# DatabaseQuerySelectFulltext::match()

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Update the query (provided to the constructor) to match the given arguments

@param string $tableName

@param string $fieldName

@param string $operator

@param string|int|array $value Value to match. Array value support added 3.0.141 (not used by PageFinder)

@return $this

@throws WireException If given $operator argument is not implemented here
