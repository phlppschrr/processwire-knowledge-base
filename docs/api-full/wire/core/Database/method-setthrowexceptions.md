# $database->setThrowExceptions($throwExceptions = true)

Source: `wire/core/Database.php`

Set whether Exceptions should be thrown on query errors

## Usage

~~~~~
// basic usage
$result = $database->setThrowExceptions();

// usage with all arguments
$result = $database->setThrowExceptions($throwExceptions = true);
~~~~~

## Arguments

- `$throwExceptions` (optional) `bool` Default is true
