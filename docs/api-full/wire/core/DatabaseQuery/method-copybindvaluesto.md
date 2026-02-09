# $databaseQuery->copyBindValuesTo($query, array $options = array()): int

Source: `wire/core/DatabaseQuery.php`

Copy bind values from this query to another given DatabaseQuery or \PDOStatement

This is a more readable interface to the getBindValues() method and does the same
thing as passing a DatabaseQuery or PDOStatement to the getBindValues() method.

## Usage

~~~~~
// basic usage
$int = $databaseQuery->copyBindValuesTo($query);

// usage with all arguments
$int = $databaseQuery->copyBindValuesTo($query, array $options = array());
~~~~~

## Arguments

- `$query` `DatabaseQuery|\PDOStatement`
- `$options` (optional) `array` Additional options - `inSQL` (string): Only copy bind values that are referenced in given SQL string

## Return value

- `int` Number of bind values that were copied

## Since

3.0.157
