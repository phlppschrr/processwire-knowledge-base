# Database

Source: `wire/core/Database.php`

Implements: `WireDatabase`

Database class provides a layer on top of mysqli

Methods:
- [`__construct(string|Config $host = 'localhost', string $user = null, string $pass = null, string $db = null, int $port = null, string $socket = null)`](method-__construct.md)
- [`query(string $sql, int $resultmode = MYSQLI_STORE_RESULT): mixed`](method-query.md)
- [`queryLog(string $sql = ''): array|bool`](method-querylog.md)
- [`getTables(): array`](method-gettables.md)
- [`isOperator(string $str): bool`](method-isoperator.md)
- [`setThrowExceptions(bool $throwExceptions = true)`](method-setthrowexceptions.md)
- [`escapeTable(string $table): string`](method-escapetable.md)
- [`escapeCol(string $col): string`](method-escapecol.md)
- [`escapeTableCol(string $str): string`](method-escapetablecol.md)
- [`escapeStr(string $str): string`](method-escapestr.md)
- [`escapeLike(string $like): string`](method-escapelike.md)
