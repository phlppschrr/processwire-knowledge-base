# WireDatabasePDO

Source: `wire/core/WireDatabasePDO.php`

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

## reset()

Reset the current PDO connection(s)

This forces re-creation of the PDO instance(s), whether writer, reader or both.
This may be useful to call after a "MySQL server has gone away" error to attempt
to re-establish the connection.


@param string|null $type
 - Specify 'writer' to reset writer instance.
 - Specify 'reader' to reset reader instance.
 - Omit or null to reset both, or whichever one is in use.

@return self

@since 3.0.240

## pdoWriter()

Return read-write (primary) PDO connection

@return \PDO

@since 3.0.175

## pdoReader()

Return read-only PDO connection if available or read/write PDO connection if not

@return \PDO

@since 3.0.175

## pdoType()

Return correct PDO instance type (reader or writer) based on given statement

@param string|\PDOStatement $query

@param bool $getName Get name of PDO type rather than instance? (default=false)

@return \PDO|string

## pdoLast()

Return last used PDO connection

@return \PDO

@since 3.0.175

## errorCode()

Fetch the SQLSTATE associated with the last operation on the statement handle


@return string

@link http://php.net/manual/en/pdostatement.errorcode.php

## errorInfo()

Fetch extended error information associated with the last operation on the database handle


@return array

@link http://php.net/manual/en/pdo.errorinfo.php

## getAttribute()

Retrieve a database connection attribute


@param int $attribute

@return mixed

@link http://php.net/manual/en/pdo.getattribute.php

## setAttribute()

Sets an attribute on the database handle


@param int $attribute

@param mixed $value

@return bool

@link http://php.net/manual/en/pdo.setattribute.php

## lastInsertId()

Returns the ID of the last inserted row or sequence value


@param string|null $name

@return string

@link http://php.net/manual/en/pdo.lastinsertid.php

## query()

Executes an SQL statement, returning a result set as a PDOStatement object


@param string $statement

@param string $note

@return \PDOStatement

@link http://php.net/manual/en/pdo.query.php

## beginTransaction()

Initiates a transaction


@return bool

@link http://php.net/manual/en/pdo.begintransaction.php

## inTransaction()

Checks if inside a transaction


@return bool

@link http://php.net/manual/en/pdo.intransaction.php

## supportsTransaction()

Are transactions available with current DB engine (or table)?


@param string $table Optionally specify a table to specifically check to that table

@return bool

## allowTransaction()

Allow a new transaction to begin right now? (i.e. supported and not already in one)

Returns combined result of supportsTransaction() === true and inTransaction() === false.


@param string $table Optional table that transaction will be for

@return bool

@since 3.0.140

## commit()

Commits a transaction


@return bool

@link http://php.net/manual/en/pdo.commit.php

## rollBack()

Rolls back a transaction


@return bool

@link http://php.net/manual/en/pdo.rollback.php

## prepare()

Prepare an SQL statement for accepting bound parameters


@param string $statement

@param array|string|bool $driver_options Optionally specify one of the following:
 - Boolean true for WireDatabasePDOStatement rather than PDOStatement (also assumed when debug mode is on) 3.0.162+
 - Driver options array
 - or you may specify the $note argument here

@param string $note Debug notes to save with query in debug mode

@return \PDOStatement|WireDatabasePDOStatement

@link http://php.net/manual/en/pdo.prepare.php

## exec()

Execute an SQL statement string

If given a PDOStatement, this method behaves the same as the execute() method.


@param string|\PDOStatement $statement

@param string $note

@return bool|int

@throws \PDOException

@link http://php.net/manual/en/pdo.exec.php

## execute()

Execute a PDO statement, with retry and error handling

Given a PDOStatement ($query) this method will execute the statement and return
true or false as to whether it was successful.

Unlike other PDO methods, this one (native to ProcessWire) will retry queries
if they failed due to a lost connection. By default it will retry up to 3 times,
but you can adjust this number as needed in the arguments.

~~~~~
// prepare the query
$query = $database->prepare("SELECT id, name FROM pages LIMIT 10");
// you can do the following, rather than native PDO $query->execute();
$database->execute($query);
~~~~~


@param \PDOStatement $query

@param bool $throw Whether or not to throw exception on query error (default=true)

@param int $maxTries Max number of times it will attempt to retry query on lost connection error

@return bool True on success, false on failure. Note if you want this, specify $throw=false in your arguments.

@throws \PDOException

## queryLog()

Log a query, start/stop query logging, or return logged queries

- To log a query, provide the $sql argument containing the query (string).
- To retrieve the query log, call this method with no arguments.
- Note the core only populates the query log when `$config->debug` mode is active.
- Specify boolean true for $sql argument to reset and start query logging (3.0.173+)
- Specify boolean false for $sql argument to stop query logging (3.0.173+)


@param string|bool $sql Query (string) to log, boolean true to reset/start query logging, boolean false to stop query logging

@param string $note Any additional debugging notes about the query

@return array|bool Returns query log array, boolean true on success, boolean false if not

## getTables()

Get array of all tables in this database.

Note that this method caches its result unless you specify boolean false for the $allowCache argument.


@param bool $allowCache Specify false if you don't want result to be cached or pulled from cache (default=true)

@return array Returns array of table names

## getColumns()

Get all columns from given table

By default returns array of column names. If verbose option is true then it returns
an array of arrays, each having 'name', 'type', 'null', 'default', and 'extra' keys,
indicating the column name, column type, whether it can be null, what it’s default value
is, and any extra information, such as whether it is auto_increment. The verbose option
also makes the return value indexed by column name (associative array).


@param string $table Table name or or `table.column` to get for specific column (when combined with verbose=true)

@param bool|int|string $verbose Include array of verbose information for each? (default=false)
 - Omit or false (bool) to just get column names.
 - True (bool) or 1 (int) to get a verbose array of information for each column, indexed by column name.
 - 2 (int) to get raw MySQL column information, indexed by column name (added 3.0.182).
 - 3 (int) to get column types as used in a CREATE TABLE statement (added 3.0.185).
 - Column name (string) to get verbose array only for only that column (added 3.0.182).

@return array

@since 3.0.180

## getIndexes()

Get all indexes from given table

By default it returns an array of index names. Specify true for the verbose option to get
index `name`, `type` and `columns` (array) for each index.


@param string $table Name of table to get indexes for or `table.index` (usually combined with verbose option).

@param bool|int|string $verbose Include array of verbose information for each? (default=false)
 - Omit or false (bool) to just get index names.
 - True (bool) or 1 (int) to get a verbose array of information for each index, indexed by index name.
 - 2 (int) to get regular PHP array of raw MySQL index information.
 - Index name (string) to get verbose array only for only that index.

@return array

@since 3.0.182

## getPrimaryKey()

Get column(s) or info for given table’s primary key/index

By default it returns a string with the column name compromising the primary key, i.e. `col1`.
If the primary key is multiple columns then it returns a CSV string, like `col1,col2,col3`.

If you specify boolean `true` for the verbose option then it returns an simplified array of
information about the primary key. If you specify integer `2` then it returns an array of
raw MySQL SHOW INDEX information.


@param string $table

@param bool|int $verbose Get array of info rather than column(s) string? (default=false)

@return string|array

@since 3.0.182

## tableExists()

Does the given table exist in this database?


@param string $table

@return bool

@since 3.0.133

## columnExists()

Does the given column exist in given table?

~~~~~
// Standard usage:
if($database->columnExists('pages', 'name')) {
  echo "The pages table has a 'name' column";
}

// You can also bundle table and column together:
if($database->columnExists('pages.name')) {
  echo "The pages table has a 'name' column";
}

$exists = $database->columnExists('pages', 'name', true);
if($exists) {
  // associative array with indexes: Name, Type, Null, Key, Default, Extra
  echo "The pages table has a 'name' column and here is verbose info: ";
  print_r($exists);
}
~~~~~


@param string $table Specify table name (or table and column name in format "table.column").

@param string $column Specify column name (or omit or blank string if already specified in $table argument).

@param bool $getInfo Return array of column info (with type info, etc.) rather than true when exists? (default=false)
  Note that the returned array is raw MySQL values from a SHOW COLUMNS command.

@return bool|array

@since 3.0.154

@throws WireDatabaseException

## indexExists()

Does table have an index with given name?

~~~~
// simple index check
if($database->indexExists('my_table', 'my_index')) {
  // index named my_index exists for my_table
}

// index check and get array of info if it exists
$info = $database->indexExists('my_table', 'my_index', true);
if($info) {
  // info is raw array of information about index from MySQL
} else {
  // index does not exist
}
~~~~


@param string $table

@param string $indexName

@param bool $getInfo Return arrays of index information rather than boolean true? (default=false)
  Note that the verbose arrays are the raw MySQL return values from a SHOW INDEX command.

@return bool|array Returns one of the following:
  - `false`: if index does not exist (regardless of $getInfo argument).
  - `true`: if index exists and $getInfo argument is omitted or false.
  - `array`: array of arrays with verbose information if index exists and $getInfo argument is true.

@since 3.0.182

## renameColumns()

Rename table columns without changing type


@param string $table

@param array $columns Associative array with one or more of `[ 'old_name' => 'new_name' ]`

@return int Number of columns renamed

@since 3.0.185

@throws \PDOException

## renameColumn()

Rename a table column without changing type


@param string $table

@param string $oldName

@param string $newName

@return bool

@throws \PDOException

@since 3.0.185

## isOperator()

Is the given string a database comparison operator?


~~~~~
if($database->isOperator('>=')) {
  // given string is a valid database operator
} else {
  // not a valid database operator
}
~~~~~

@param string $str 1-2 character operator to test

@param bool|null|int $operatorType Specify a WireDatabasePDO::operatorType* constant (3.0.162+), or any one of the following (3.0.143+):
 - `NULL`: allow all operators (default value if not specified)
 - `FALSE`: allow only comparison operators
 - `TRUE`: allow only bitwise operators

@param bool $get Return the operator rather than true, when valid? (default=false) Added 3.0.162

@return bool True if valid, false if not

## isStopword()

Is given word a fulltext stopword for database engine?


@param string $word

@param string $engine DB engine ('myisam' or 'innodb') or omit for current engine

@return bool

@since 3.0.160

## getStopwords()

Get all fulltext stopwords for database engine


@param string $engine Specify DB engine of "myisam" or "innodb" or omit for current DB engine

@param bool $flip Return flipped array where stopwords are array keys rather than values? for isset() use (default=false)

@return array

## escapeTable()

Sanitize a table name for _a-zA-Z0-9


@param string $table String containing table name

@return string Sanitized table name

## escapeCol()

Sanitize a column name for _a-zA-Z0-9


@param string $col

@return string

## escapeTableCol()

Sanitize a table.column string, where either part is optional


@param string $str

@return string

@throws WireDatabaseException

## escapeOperator()

Sanitize comparison operator


@param string $operator

@param bool|int|null $operatorType Specify a WireDatabasePDO::operatorType* constant (default=operatorTypeComparison)

@param string $default Default/fallback operator to return if given one is not valid (default='=')

@return string

## escapeStr()

Escape a string value, same as $database->quote() but without surrounding quotes


@param string $str

@return string

## quote()

Quote and escape a string value


@param string $str

@return string

@link http://php.net/manual/en/pdo.quote.php

## escapeLike()

Escape a string value, plus escape characters necessary for a MySQL 'LIKE' phrase


@param string $like

@return string

## __get()

@param string $name

@return mixed|null|\PDO

## closeConnection()

Close the PDO connection

## getVariable()

Get the value of a MySQL variable

~~~~~
// Get the minimum fulltext index word length
$value = $database->getVariable('ft_min_word_len');
echo $value; // outputs "4"
~~~~~


@param string $name Name of MySQL variable you want to retrieve

@param bool $cache Allow use of cached values? (default=true)

@param bool $sub Allow substitution of MyISAM variable names to InnoDB equivalents when InnoDB is engine? (default=true)

@return string|null

## getVersion()

Get MySQL/MariaDB version

Example return values:

 - 5.7.23
 - 10.1.34-MariaDB


@return string

@param bool $getNumberOnly Get only version number, exclude any vendor specific suffixes? (default=false) 3.0.185+

@since 3.0.166

## getServerType()

Get server type, one of MySQL, MariDB, Percona, etc.


@return string

@since 3.0.185

## getRegexEngine()

Get the regular expression engine used by database

Returns one of 'ICU' (MySQL 8.0.4+) or 'HenrySpencer' (earlier versions and MariaDB)


@return string

@since 3.0.166

@todo this will need to be updated when/if MariaDB adds version that uses ICU engine

## getEngine()

Get current database engine (lowercase)


@return string

@since 3.0.160

## getCharset()

Get current database charset (lowercase)


@return string

@since 3.0.160

## backups()

Retrieve new instance of WireDatabaseBackups ready to use with this connection

See `WireDatabaseBackup` class for usage.


@return WireDatabaseBackup

@throws WireException|\Exception on fatal error

@see WireDatabaseBackup::backup(), WireDatabaseBackup::restore()

## getMaxIndexLength()

Get max length allowed for a fully indexed varchar column in ProcessWire


@return int

## sqlMode()

Get SQL mode, set SQL mode, add to existing SQL mode, or remove from existing SQL mode


~~~~~
// Get SQL mode
$mode = $database->sqlMode();

// Add an SQL mode
$database->sqlMode('add', 'STRICT_TRANS_TABLES');

// Remove SQL mode if version at least 5.7.0
$database->sqlMode('remove', 'ONLY_FULL_GROUP_BY', '5.7.0');
~~~~~

@param string $action Specify "get", "set", "add" or "remove". (default="get")

@param string $mode Mode string or CSV string with SQL mode(s), i.e. "STRICT_TRANS_TABLES,ONLY_FULL_GROUP_BY".
  This argument should be omitted when using the "get" action.

@param string $minVersion Make the given action only apply if MySQL version is at least $minVersion, i.e. "5.7.0".

@param \PDO PDO connection to use or omit for current (default=null) 3.0.175+

@return string|bool Returns string in "get" action, boolean false if required version not present, or true otherwise.

@throws WireException If given an invalid $action

## getTime()

Get current date/time ISO-8601 string or UNIX timestamp according to database


@param bool $getTimestamp Get unix timestamp rather than ISO-8601 string? (default=false)

@return string|int

@since 3.0.183
