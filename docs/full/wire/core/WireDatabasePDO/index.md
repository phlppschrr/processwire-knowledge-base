# WireDatabasePDO

Source: `wire/core/WireDatabasePDO.php`

Inherits: `Wire`
Implements: `WireDatabase`

Database class provides a layer on top of mysqli

All database operations in ProcessWire are performed via this PDO-style database class.
ProcessWire creates the database connection automatically at boot and this is available from the `$database` API variable.
If you want to create a new connection on your own, choose either option A or B below:
~~~~~
// The following are required to construct a WireDatabasePDO
$dsn = 'mysql:dbname=mydb;host=myhost;port=3306';
$username = 'username';
$password = 'password';
$driver_options = []; // optional

// Construct option A
$db = new WireDatabasePDO($dsn, $username, $password, $driver_options);

// Construct option B
$db = new WireDatabasePDO([
  'dsn' => $dsn,
  'user' => $username,
  'pass' => $password,
  'options' => $driver_options, // optional
  'reader' => [ // optional
    'dsn' => '…',
    …
  ],
  …
]);
~~~~~

Methods:
- [`reset(string|null $type = null): self`](method-reset.md)
- [`pdoWriter(): \PDO`](method-pdowriter.md)
- [`pdoReader(): \PDO`](method-pdoreader.md)
- [`pdoType(string|\PDOStatement &$query, bool $getName = false): \PDO|string`](method-pdotype.md)
- [`pdoLast(): \PDO`](method-pdolast.md)
- [`errorCode(): string`](method-errorcode.md)
- [`errorInfo(): array`](method-errorinfo.md)
- [`getAttribute(int $attribute): mixed`](method-getattribute.md)
- [`setAttribute(int $attribute, mixed $value): bool`](method-setattribute.md)
- [`lastInsertId(string|null $name = null): string`](method-lastinsertid.md)
- [`query(string $statement, string $note = ''): \PDOStatement`](method-query.md)
- [`beginTransaction(): bool`](method-begintransaction.md)
- [`inTransaction(): bool`](method-intransaction.md)
- [`supportsTransaction(string $table = ''): bool`](method-supportstransaction.md)
- [`allowTransaction(string $table = ''): bool`](method-allowtransaction.md)
- [`commit(): bool`](method-commit.md)
- [`rollBack(): bool`](method-rollback.md)
- [`prepare(string $statement, array|string|bool $driver_options = array(), string $note = ''): \PDOStatement|WireDatabasePDOStatement`](method-prepare.md)
- [`exec(string|\PDOStatement $statement, string $note = ''): bool|int`](method-exec.md)
- [`execute(\PDOStatement $query, bool $throw = true, int $maxTries = 3): bool`](method-execute.md)
- [`queryLog(string|bool|int $sql = '', string $note = ''): array|bool`](method-querylog.md)
- [`getTables(bool $allowCache = true): array`](method-gettables.md)
- [`getColumns(string $table, bool|int|string $verbose = false): array`](method-getcolumns.md)
- [`getIndexes(string $table, bool|int|string $verbose = false): array`](method-getindexes.md)
- [`getPrimaryKey(string $table, bool|int $verbose = false): string|array`](method-getprimarykey.md)
- [`tableExists(string $table): bool`](method-tableexists.md)
- [`columnExists(string $table, string $column = '', bool $getInfo = false): bool|array`](method-columnexists.md)
- [`indexExists(string $table, string $indexName, bool $getInfo = false): bool|array`](method-indexexists.md)
- [`renameColumns(string $table, array $columns): int`](method-renamecolumns.md)
- [`renameColumn(string $table, string $oldName, string $newName): bool`](method-renamecolumn.md)
- [`isOperator(string $str, bool|null|int $operatorType = self::operatorTypeAny, bool $get = false): bool`](method-isoperator.md)
- [`isStopword(string $word, string $engine = ''): bool`](method-isstopword.md)
- [`getStopwords(string $engine = '', bool $flip = false): array`](method-getstopwords.md)
- [`escapeTable(string $table): string`](method-escapetable.md)
- [`escapeCol(string $col): string`](method-escapecol.md)
- [`escapeTableCol(string $str): string`](method-escapetablecol.md)
- [`escapeOperator(string $operator, bool|int|null $operatorType = self::operatorTypeComparison, string $default = '='): string`](method-escapeoperator.md)
- [`escapeStr(string $str): string`](method-escapestr.md)
- [`quote(string $str): string`](method-quote.md)
- [`escapeLike(string $like): string`](method-escapelike.md)
- [`__get(string $name): mixed|null|\PDO`](method-__get.md)
- [`closeConnection()`](method-closeconnection.md)
- [`getVariable(string $name, bool $cache = true, bool $sub = true): string|null`](method-getvariable.md)
- [`getVersion(bool $getNumberOnly = false): string`](method-getversion.md)
- [`getServerType(): string`](method-getservertype.md)
- [`getRegexEngine(): string`](method-getregexengine.md)
- [`getEngine(): string`](method-getengine.md)
- [`getCharset(): string`](method-getcharset.md)
- [`backups(): WireDatabaseBackup`](method-backups.md)
- [`getMaxIndexLength(): int`](method-getmaxindexlength.md)
- [`sqlMode(string $action = 'get', string $mode = '', string $minVersion = '', $pdo = null): string|bool`](method-sqlmode.md)
- [`getTime(bool $getTimestamp = false): string|int`](method-gettime.md)
