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
Method: [reset()](method-reset.md)
Method: [pdoWriter()](method-pdowriter.md)
Method: [pdoReader()](method-pdoreader.md)
Method: [pdoType()](method-pdotype.md)
Method: [pdoLast()](method-pdolast.md)
Method: [errorCode()](method-errorcode.md)
Method: [errorInfo()](method-errorinfo.md)
Method: [getAttribute()](method-getattribute.md)
Method: [setAttribute()](method-setattribute.md)
Method: [lastInsertId()](method-lastinsertid.md)
Method: [query()](method-query.md)
Method: [beginTransaction()](method-begintransaction.md)
Method: [inTransaction()](method-intransaction.md)
Method: [supportsTransaction()](method-supportstransaction.md)
Method: [allowTransaction()](method-allowtransaction.md)
Method: [commit()](method-commit.md)
Method: [rollBack()](method-rollback.md)
Method: [prepare()](method-prepare.md)
Method: [exec()](method-exec.md)
Method: [execute()](method-execute.md)
Method: [queryLog()](method-querylog.md)
Method: [getTables()](method-gettables.md)
Method: [getColumns()](method-getcolumns.md)
Method: [getIndexes()](method-getindexes.md)
Method: [getPrimaryKey()](method-getprimarykey.md)
Method: [tableExists()](method-tableexists.md)
Method: [columnExists()](method-columnexists.md)
Method: [indexExists()](method-indexexists.md)
Method: [renameColumns()](method-renamecolumns.md)
Method: [renameColumn()](method-renamecolumn.md)
Method: [isOperator()](method-isoperator.md)
Method: [isStopword()](method-isstopword.md)
Method: [getStopwords()](method-getstopwords.md)
Method: [escapeTable()](method-escapetable.md)
Method: [escapeCol()](method-escapecol.md)
Method: [escapeTableCol()](method-escapetablecol.md)
Method: [escapeOperator()](method-escapeoperator.md)
Method: [escapeStr()](method-escapestr.md)
Method: [quote()](method-quote.md)
Method: [escapeLike()](method-escapelike.md)
Method: [__get()](method-__get.md)
Method: [closeConnection()](method-closeconnection.md)
Method: [getVariable()](method-getvariable.md)
Method: [getVersion()](method-getversion.md)
Method: [getServerType()](method-getservertype.md)
Method: [getRegexEngine()](method-getregexengine.md)
Method: [getEngine()](method-getengine.md)
Method: [getCharset()](method-getcharset.md)
Method: [backups()](method-backups.md)
Method: [getMaxIndexLength()](method-getmaxindexlength.md)
Method: [sqlMode()](method-sqlmode.md)
Method: [getTime()](method-gettime.md)
