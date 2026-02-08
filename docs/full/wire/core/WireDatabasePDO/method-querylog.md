# $wireDatabasePDO->queryLog($sql = '', $note = ''): array|bool

Source: `wire/core/WireDatabasePDO.php`

Log a query, start/stop query logging, or return logged queries

- To log a query, provide the $sql argument containing the query (string).
- To retrieve the query log, call this method with no arguments.
- Note the core only populates the query log when `$config->debug` mode is active.
- Specify boolean true for $sql argument to reset and start query logging (3.0.173+)
- Specify integer 1 for $sql argument to start query logging without reset (3.0.256+)
- Specify boolean false for $sql argument to stop query logging (3.0.173+)

## Usage

~~~~~
// basic usage
$array = $wireDatabasePDO->queryLog();

// usage with all arguments
$array = $wireDatabasePDO->queryLog($sql = '', $note = '');
~~~~~

## Arguments

- `$sql` (optional) `string|bool|int` Query to log, `true` to reset+start log, `1` to start w/no reset, `false` to stop, omit to get log.
- `$note` (optional) `string` Any additional debugging notes about the query

## Return value

- `array|bool` Returns query log array, boolean true on success, boolean false if not
