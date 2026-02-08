# DatabaseQuery::copyBindValuesTo()

Source: `wire/core/DatabaseQuery.php`

Copy bind values from this query to another given DatabaseQuery or \PDOStatement

This is a more readable interface to the getBindValues() method and does the same
thing as passing a DatabaseQuery or PDOStatement to the getBindValues() method.

@param DatabaseQuery|\PDOStatement $query

@param array $options Additional options
 - `inSQL` (string): Only copy bind values that are referenced in given SQL string

@return int Number of bind values that were copied

@since 3.0.157
