# WireDatabasePDOStatement

Source: `wire/core/WireDatabasePDOStatement.php`

ProcessWire PDO Statement

Serves as a wrapper to PHP’s PDOStatement class, purely for debugging purposes.
When ProcessWire is not in debug mode, this class is not used at present.

The primary thing this class does is log queries with the bind parameters
populated into the SQL query string, purely for readability purposes. These
populated queries are not ever used for actual database queries, just for logs.

Note that this class only tracks bindValue() and does not track bindParam().

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

Methods:
Method: [__construct()](method-__construct.md)
Method: [setDebugNote()](method-setdebugnote.md)
Method: [setDebugParam()](method-setdebugparam.md)
Method: [bindValue()](method-bindvalue.md)
Method: [execute()](method-execute.md)
Method: [executeDebug()](method-executedebug.md)
