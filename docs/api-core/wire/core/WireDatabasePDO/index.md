# WireDatabasePDO

Source: `wire/core/WireDatabasePDO.php`

Inherits: `Wire`
Implements: `WireDatabase`

## Summary

Database class provides a layer on top of mysqli

Common methods:
- [`getInstance()`](method-getinstance.md)
- [`_init()`](method-_init.md)
- [`reset()`](method-reset.md)
- [`close()`](method-close.md)
- [`pdo()`](method-pdo.md)

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

## Methods
- [`reset(string|null $type = null): self`](method-reset.md) Reset the current PDO connection(s)
- [`pdoWriter(): \PDO`](method-pdowriter.md) Return read-write (primary) PDO connection
- [`pdoReader(): \PDO`](method-pdoreader.md) Return read-only PDO connection if available or read/write PDO connection if not
- [`pdoType(string|\PDOStatement &$query, bool $getName = false): \PDO|string`](method-pdotype.md) Return correct PDO instance type (reader or writer) based on given statement
- [`pdoLast(): \PDO`](method-pdolast.md) Return last used PDO connection
- [`errorCode(): string`](method-errorcode.md) Fetch the SQLSTATE associated with the last operation on the statement handle
- [`errorInfo(): array`](method-errorinfo.md) Fetch extended error information associated with the last operation on the database handle
- [`getAttribute(int $attribute): mixed`](method-getattribute.md) Retrieve a database connection attribute
- [`setAttribute(int $attribute, mixed $value): bool`](method-setattribute.md) Sets an attribute on the database handle
- [`lastInsertId(string|null $name = null): string`](method-lastinsertid.md) Returns the ID of the last inserted row or sequence value
- [`query(string $statement, string $note = ''): \PDOStatement`](method-query.md) Executes an SQL statement, returning a result set as a PDOStatement object
- [`beginTransaction(): bool`](method-begintransaction.md) Initiates a transaction
- [`inTransaction(): bool`](method-intransaction.md) Checks if inside a transaction
- [`supportsTransaction(string $table = ''): bool`](method-supportstransaction.md) Are transactions available with current DB engine (or table)?
- [`allowTransaction(string $table = ''): bool`](method-allowtransaction.md) Allow a new transaction to begin right now? (i.e. supported and not already in one)
- [`commit(): bool`](method-commit.md) Commits a transaction
- [`rollBack(): bool`](method-rollback.md) Rolls back a transaction
- [`prepare(string $statement, array|string|bool $driver_options = array(), string $note = ''): \PDOStatement|WireDatabasePDOStatement`](method-prepare.md) Prepare an SQL statement for accepting bound parameters
- [`exec(string|\PDOStatement $statement, string $note = ''): bool|int`](method-exec.md) Execute an SQL statement string
- [`execute(\PDOStatement $query, bool $throw = true, int $maxTries = 3): bool`](method-execute.md) Execute a PDO statement, with retry and error handling
- [`queryLog(string|bool|int $sql = '', string $note = ''): array|bool`](method-querylog.md) Log a query, start/stop query logging, or return logged queries
- [`getTables(bool $allowCache = true): array`](method-gettables.md) Get array of all tables in this database.
- [`getColumns(string $table, bool|int|string $verbose = false): array`](method-getcolumns.md) Get all columns from given table
- [`getIndexes(string $table, bool|int|string $verbose = false): array`](method-getindexes.md) Get all indexes from given table
- [`getPrimaryKey(string $table, bool|int $verbose = false): string|array`](method-getprimarykey.md) Get column(s) or info for given table’s primary key/index
- [`tableExists(string $table): bool`](method-tableexists.md) Does the given table exist in this database?
- [`columnExists(string $table, string $column = '', bool $getInfo = false): bool|array`](method-columnexists.md) Does the given column exist in given table?
- [`indexExists(string $table, string $indexName, bool $getInfo = false): bool|array`](method-indexexists.md) Does table have an index with given name?
- [`renameColumns(string $table, array $columns): int`](method-renamecolumns.md) Rename table columns without changing type
- [`renameColumn(string $table, string $oldName, string $newName): bool`](method-renamecolumn.md) Rename a table column without changing type
- [`isOperator(string $str, bool|null|int $operatorType = self::operatorTypeAny, bool $get = false): bool`](method-isoperator.md) Is the given string a database comparison operator?
- [`isStopword(string $word, string $engine = ''): bool`](method-isstopword.md) Is given word a fulltext stopword for database engine?
- [`getStopwords(string $engine = '', bool $flip = false): array`](method-getstopwords.md) Get all fulltext stopwords for database engine
- [`escapeTable(string $table): string`](method-escapetable.md) Sanitize a table name for _a-zA-Z0-9
- [`escapeCol(string $col): string`](method-escapecol.md) Sanitize a column name for _a-zA-Z0-9
- [`escapeTableCol(string $str): string`](method-escapetablecol.md) Sanitize a table.column string, where either part is optional
- [`escapeOperator(string $operator, bool|int|null $operatorType = self::operatorTypeComparison, string $default = '='): string`](method-escapeoperator.md) Sanitize comparison operator
- [`escapeStr(string $str): string`](method-escapestr.md) Escape a string value, same as `$database->quote()` but without surrounding quotes
- [`quote(string $str): string`](method-quote.md) Quote and escape a string value
- [`escapeLike(string $like): string`](method-escapelike.md) Escape a string value, plus escape characters necessary for a MySQL 'LIKE' phrase
- [`__get(string $name): mixed|null|\PDO`](method-__get.md)
- [`closeConnection()`](method-closeconnection.md) Close the PDO connection
- [`getVariable(string $name, bool $cache = true, bool $sub = true): string|null`](method-getvariable.md) Get the value of a MySQL variable
- [`getVersion(bool $getNumberOnly = false): string`](method-getversion.md) Get MySQL/MariaDB version
- [`getServerType(): string`](method-getservertype.md) Get server type, one of MySQL, MariDB, Percona, etc.
- [`getRegexEngine(): string`](method-getregexengine.md) Get the regular expression engine used by database
- [`getEngine(): string`](method-getengine.md) Get current database engine (lowercase)
- [`getCharset(): string`](method-getcharset.md) Get current database charset (lowercase)
- [`backups(): WireDatabaseBackup`](method-backups.md) Retrieve new instance of WireDatabaseBackups ready to use with this connection
- [`getMaxIndexLength(): int`](method-getmaxindexlength.md) Get max length allowed for a fully indexed varchar column in ProcessWire
- [`sqlMode(string $action = 'get', string $mode = '', string $minVersion = '', $pdo = null): string|bool`](method-sqlmode.md) Get SQL mode, set SQL mode, add to existing SQL mode, or remove from existing SQL mode
- [`getTime(bool $getTimestamp = false): string|int`](method-gettime.md) Get current date/time ISO-8601 string or UNIX timestamp according to database
