# $database->queryLog($sql = ''): array|bool

Source: `wire/core/Database.php`

Log a query or return the query log

## Usage

~~~~~
// basic usage
$array = $database->queryLog();

// usage with all arguments
$array = $database->queryLog($sql = '');
~~~~~

## Arguments

- `$sql` (optional) `string` Omit to instead return the query log

## Return value

- `array|bool` Returns query log array when $sql argument is omitted
