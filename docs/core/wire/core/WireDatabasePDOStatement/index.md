# WireDatabasePDOStatement

Source: `wire/core/WireDatabasePDOStatement.php`

ProcessWire PDO Statement

Serves as a wrapper to PHP’s PDOStatement class, purely for debugging purposes.
When ProcessWire is not in debug mode, this class is not used at present.

The primary thing this class does is log queries with the bind parameters
populated into the SQL query string, purely for readability purposes. These
populated queries are not ever used for actual database queries, just for logs.

Note that this class only tracks bindValue() and does not track bindParam().

Methods:
- [`__construct(WireDatabasePDO $database)`](method-__construct.md)
- [`setDebugNote(string $note)`](method-setdebugnote.md)
- [`setDebugParam(string $parameter, int|string|null $value, int|null $data_type = null)`](method-setdebugparam.md)
- [`bindValue(string|int $parameter, mixed $value, int $data_type = \PDO::PARAM_STR): bool`](method-bindvalue.md)
- [`execute(array|null $input_parameters = NULL): bool`](method-execute.md)
- [`executeDebug(array|null $input_parameters = NULL): bool`](method-executedebug.md)
