# DatabaseQuery

Source: `wire/core/DatabaseQuery.php`

ProcessWire DatabaseQuery

Serves as a base class for other DatabaseQuery classes

The intention behind these classes is to have a query that can safely
be passed between methods and objects that add to it without knowledge
of what other methods/objects have done to it. It also means being able
to build a complex query without worrying about correct syntax placement.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## other

@property array $where

@property array $bindValues

@property array $bindKeys

@property array $bindOptions

@property string $query

@property string $sql

@method $this where($sql, array $params = array())

## __construct()

Construct

## bindOption()

Get or set a bind option

@param string|bool $optionName One of 'prefix' or 'global', boolean true to get/set all

@param null|int|string|array $optionValue Omit when getting, Specify option value to set, or array when setting all

@return string|int|array

@since 3.0.157

## bindValue()

Bind a parameter value

@param string $key Parameter name

@param mixed $value Parameter value

@param null|int|string Optionally specify value type: string, int, bool, null or PDO::PARAM_* constant.

@return $this

## bindValueGetKey()

Bind value and get unique key that refers to it in one step

@param string|int|float $value

@param null|int|string $type

@return string

@since 3.0.157

## getUniqueBindKey()

Get a unique key to use for bind value

Note if you given a `key` option, it will only be used if it is determined unique,
otherwise it’ll auto-generate one. When using your specified key, it is the only
option that applies, unless it is not unique and the method has to auto-generate one.

@param array $options
 - `key` (string): Preferred bind key, or omit (blank) to auto-generate (digit only keys not accepted)
 - `value` (string|int): Value to use as part of the generated key
 - `prefix` (string): Prefix to override default
 - `global` (bool): Require globally unique among all instances?

@return string Returns bind key/name in format ":name" (with leading colon)

@since 3.0.156

## getBindValues()

Get bind values, with options

- If given a \PDOStatement or DatabaseQuery, it is assumed to be the `query` option.
- When copying, you may prefer to use the copyBindValuesTo() method instead (more readable).

Note: The $options argument was added in 3.0.156, prior to this it was a $method argument,
which was never used so has been removed.

@param string|\PDOStatement|DatabaseQuery|array $options Optionally specify an option:
 - `query` (\PDOStatement|DatabaseQuery): Copy bind values to this query object (default=null)
 - `count` (bool): Get a count of values rather than array of values (default=false) 3.0.157+
 - `inSQL` (string): Only get bind values referenced in this given SQL statement

@return array|int Returns one of the following:
 - Associative array in format [ ":column" => "value" ] where each "value" is int, string or NULL.
 - if `count` option specified as true then it returns a count of values instead.

## copyBindValuesTo()

Copy bind values from this query to another given DatabaseQuery or \PDOStatement

This is a more readable interface to the getBindValues() method and does the same
thing as passing a DatabaseQuery or PDOStatement to the getBindValues() method.

@param DatabaseQuery|\PDOStatement $query

@param array $options Additional options
 - `inSQL` (string): Only copy bind values that are referenced in given SQL string

@return int Number of bind values that were copied

@since 3.0.157

## copyTo()

Copy queries from this DatabaseQuery to another DatabaseQuery

If you want to copy bind values you should also call copyBindValuesTo($query) afterwards.

@param DatabaseQuery $query Query to copy data to

@param array $methods Optionally specify the names of methods to copy, otherwise all are copied

@return int Total items copied

@since 3.0.157

## __call()

Enables calling the various parts of a query as functions for a fluent interface.

Examples (all in context of DatabaseQuerySelect):
~~~~~
$query->select("id")->from("mytable")->orderby("name");
~~~~~
To bind one or more named parameters, specify associative array as second argument:
~~~~~
$query->where("name=:name", [ ':name' => $page->name ]);
~~~~~
To bind one or more implied parameters, use question marks and specify regular array:
~~~~~
$query->where("name=?, id=?", [ $page->name, $page->id ]);
~~~~~
When there is only one implied parameter, specifying an array is optional:
~~~~~
$query->where("name=?", $page->name);
~~~~~

The "select" or "where" methods above may be any method supported by the class.
Implied parameters (using "?") was added in 3.0.157.

@param string $method

@param array $arguments

@return $this

## __set()

@param string $key

@param mixed $value

## __get()

@param string $key

@return array|mixed|null

## getQuery()

Generate the SQL query based on everything set in this DatabaseQuery object

@return string

## getDebugQuery()

Get SQL query with bind params populated for debugging purposes (not to be used as actual query)

@return string

## getSQL()

Return generated SQL for entire query or specific method

@param string $method Optionally specify method name to get SQL for

@return string

@since 3.0.157

## getQueryMethod()

Return the generated SQL for specific query method

@param string $method Specify method name to get SQL for, or blank string for entire query

@return string

@since 3.0.157

## prepare()

Get the WHERE portion of the query

protected function getQueryWhere() {
$where = $this->where;
if(!count($where)) return '';
$sql = "\nWHERE " . implode(" \nAND ", $where)  . " ";
return $sql;
}

## prepare()

Prepare and return a PDOStatement

@return \PDOStatement

## pdoParamType()

Get the PDO::PARAM_* type for given value

@param string|int|null $value

@return int

## execute()

Execute the query with the current database handle

@param array $options
 - `throw` (bool): Throw exceptions? (default=true)
 - `maxTries` (int): Max times to retry if connection lost during query. (default=3)
 - `returnQuery` (bool): Return PDOStatement query? If false, returns bool result of execute. (default=true)

@return \PDOStatement|bool

@throws WireDatabaseQueryException|\PDOException
