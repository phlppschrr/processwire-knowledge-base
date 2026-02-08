# $wireDatabasePDO->reset($type = null): self

Source: `wire/core/WireDatabasePDO.php`

Reset the current PDO connection(s)

This forces re-creation of the PDO instance(s), whether writer, reader or both.
This may be useful to call after a "MySQL server has gone away" error to attempt
to re-establish the connection.

## Arguments

- string|null $type - Specify 'writer' to reset writer instance. - Specify 'reader' to reset reader instance. - Omit or null to reset both, or whichever one is in use.

## Return value

self

## Meta

- @since 3.0.240
