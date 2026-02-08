# $wireDatabasePDO->allowTransaction($table = ''): bool

Source: `wire/core/WireDatabasePDO.php`

Allow a new transaction to begin right now? (i.e. supported and not already in one)

Returns combined result of supportsTransaction() === true and inTransaction() === false.

## Arguments

- string $table Optional table that transaction will be for

## Return value

bool

## Meta

- @since 3.0.140
