# Database

Source: `wire/core/Database.php`

Implements: `WireDatabase`

Database class provides a layer on top of mysqli

Methods:
- [`__construct(string|Config $host = 'localhost', string $user = null, string $pass = null, string $db = null, int $port = null, string $socket = null)`](method-__construct.md) Construct the Database
- [`query(string $sql, int $resultmode = MYSQLI_STORE_RESULT): mixed`](method-query.md) Overrides default mysqli query method so that it also records and times queries.
- [`queryLog(string $sql = ''): array|bool`](method-querylog.md) Log a query or return the query log
- [`getTables(): array`](method-gettables.md) Get array of all tables in this database.
- [`isOperator(string $str): bool`](method-isoperator.md) Is the given string a database comparison operator?
- [`setThrowExceptions(bool $throwExceptions = true)`](method-setthrowexceptions.md) Set whether Exceptions should be thrown on query errors
- [`escapeTable(string $table): string`](method-escapetable.md) Sanitize a table name for _a-zA-Z0-9
- [`escapeCol(string $col): string`](method-escapecol.md) Sanitize a column name for _a-zA-Z0-9
- [`escapeTableCol(string $str): string`](method-escapetablecol.md) Sanitize a table.column string, where either part is optional
- [`escapeStr(string $str): string`](method-escapestr.md) Escape a string value, camelCase alias of escape_string()
- [`escapeLike(string $like): string`](method-escapelike.md) Escape a string value, plus escape characters necessary for a MySQL 'LIKE' phrase
