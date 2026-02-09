# $wireDatabasePDO->lastInsertId($name = null): string

Source: `wire/core/WireDatabasePDO.php`

Returns the ID of the last inserted row or sequence value

## Usage

~~~~~
// basic usage
$string = $wireDatabasePDO->lastInsertId();

// usage with all arguments
$string = $wireDatabasePDO->lastInsertId($name = null);
~~~~~

## Arguments

- `$name` (optional) `string|null`

## Return value

- `string`

## Details

- @link http://php.net/manual/en/pdo.lastinsertid.php
