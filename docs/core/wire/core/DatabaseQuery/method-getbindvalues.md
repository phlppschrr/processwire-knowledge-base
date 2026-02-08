# DatabaseQuery::getBindValues()

Source: `wire/core/DatabaseQuery.php`

Get bind values, with options

- If given a \PDOStatement or DatabaseQuery, it is assumed to be the `query` option.
- When copying, you may prefer to use the copyBindValuesTo() method instead (more readable).

Note: The $options argument was added in 3.0.156, prior to this it was a $method argument,
which was never used so has been removed.

@param string|\PDOStatement|DatabaseQuery|array $options Optionally specify an option:
 - `query` (\PDOStatement|DatabaseQuery): Copy bind values to this query object (default=null)
 - `count` (bool): Get a count of values rather than array of values (default=false) 3.0.157+
 - `inSQL` (string): Only get bind values referenced in this given SQL statement

@return array|int Returns one of the following:
 - Associative array in format [ ":column" => "value" ] where each "value" is int, string or NULL.
 - if `count` option specified as true then it returns a count of values instead.
