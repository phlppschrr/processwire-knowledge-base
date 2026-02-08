# $wireDataDB->delete($name): int

Source: `wire/core/WireDataDB.php`

Delete meta value or all meta values (if you specify true)

## Usage

~~~~~
// basic usage
$int = $wireDataDB->delete($name);
~~~~~

## Arguments

- `$name` `string|bool` Meta property name to delete or specify boolean true for all

## Return value

- `int` Number of rows deleted

## Exceptions

- `WireException`
