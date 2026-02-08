# DatabaseQuery::execute()

Source: `wire/core/DatabaseQuery.php`

Execute the query with the current database handle

@param array $options
 - `throw` (bool): Throw exceptions? (default=true)
 - `maxTries` (int): Max times to retry if connection lost during query. (default=3)
 - `returnQuery` (bool): Return PDOStatement query? If false, returns bool result of execute. (default=true)

@return \PDOStatement|bool

@throws WireDatabaseQueryException|\PDOException
