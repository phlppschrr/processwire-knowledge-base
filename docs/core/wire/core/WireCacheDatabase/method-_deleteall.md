# $wireCacheDatabase->_deleteAll($expireAll = false): int

Source: `wire/core/WireCacheDatabase.php`

Implementation for deleteAll and expireAll methods

## Usage

~~~~~
// basic usage
$int = $wireCacheDatabase->_deleteAll();

// usage with all arguments
$int = $wireCacheDatabase->_deleteAll($expireAll = false);
~~~~~

## Arguments

- `$expireAll` (optional) `bool`

## Return value

- `int`

## Exceptions

- `WireException`
