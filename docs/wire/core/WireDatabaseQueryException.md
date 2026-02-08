# WireDatabaseQueryException

Source: `wire/core/Exceptions.php`

Thrown by DatabaseQuery classes on query exception

May have \PDOException populated with call to its getPrevious(); method,
in which can it also has same getCode() and getMessage() as \PDOException.
Use getCodeStr() for PDOException string code.

@since 3.0.156
