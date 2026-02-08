# $wireDatabasePDO->execute(\PDOStatement $query, $throw = true, $maxTries = 3): bool

Source: `wire/core/WireDatabasePDO.php`

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

## Arguments

- \PDOStatement $query
- bool $throw Whether or not to throw exception on query error (default=true)
- int $maxTries Max number of times it will attempt to retry query on lost connection error

## Return value

bool True on success, false on failure. Note if you want this, specify $throw=false in your arguments.

## Throws

- \PDOException
