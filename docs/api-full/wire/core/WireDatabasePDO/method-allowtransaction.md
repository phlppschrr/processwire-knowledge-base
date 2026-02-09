# $wireDatabasePDO->allowTransaction($table = ''): bool

Source: `wire/core/WireDatabasePDO.php`

Allow a new transaction to begin right now? (i.e. supported and not already in one)

Returns combined result of supportsTransaction() === true and inTransaction() === false.

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDO->allowTransaction();

// usage with all arguments
$bool = $wireDatabasePDO->allowTransaction($table = '');
~~~~~

## Arguments

- `$table` (optional) `string` Optional table that transaction will be for

## Return value

- `bool`

## Since

3.0.140
