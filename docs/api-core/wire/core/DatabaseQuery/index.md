# DatabaseQuery

Source: `wire/core/DatabaseQuery.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

ProcessWire DatabaseQuery

Serves as a base class for other DatabaseQuery classes

The intention behind these classes is to have a query that can safely
be passed between methods and objects that add to it without knowledge
of what other methods/objects have done to it. It also means being able
to build a complex query without worrying about correct syntax placement.


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct()`](method-__construct.md) Construct
- [`bindOption(string|bool $optionName, null|int|string|array $optionValue = null): string|int|array`](method-bindoption.md) Get or set a bind option
- [`bindValue(string $key, mixed $value, $type = null): $this`](method-bindvalue.md) Bind a parameter value
- [`bindValueGetKey(string|int|float $value, null|int|string $type = null): string`](method-bindvaluegetkey.md) Bind value and get unique key that refers to it in one step
- [`getUniqueBindKey(array $options = array()): string`](method-getuniquebindkey.md) Get a unique key to use for bind value
- [`getBindValues(string|\PDOStatement|DatabaseQuery|array $options = array()): array|int`](method-getbindvalues.md) Get bind values, with options
- [`copyBindValuesTo(DatabaseQuery|\PDOStatement $query, array $options = array()): int`](method-copybindvaluesto.md) Copy bind values from this query to another given DatabaseQuery or \PDOStatement
- [`copyTo(DatabaseQuery $query, array $methods = array()): int`](method-copyto.md) Copy queries from this DatabaseQuery to another DatabaseQuery
- [`__call(string $method, array $arguments): $this`](method-__call.md) Enables calling the various parts of a query as functions for a fluent interface.
- [`__set(string $key, mixed $value)`](method-__set.md)
- [`__get(string $key): array|mixed|null`](method-__get.md)
- [`getQuery(): string`](method-getquery.md) Generate the SQL query based on everything set in this DatabaseQuery object
- [`getDebugQuery(): string`](method-getdebugquery.md) Get SQL query with bind params populated for debugging purposes (not to be used as actual query)
- [`getSQL(string $method = ''): string`](method-getsql.md) Return generated SQL for entire query or specific method
- [`getQueryMethod(string $method): string`](method-getquerymethod.md) Return the generated SQL for specific query method
- [`prepare()`](method-prepare.md) Get the WHERE portion of the query
- [`prepare(): \PDOStatement`](method-prepare.md) Prepare and return a PDOStatement
- [`pdoParamType(string|int|null $value): int`](method-pdoparamtype.md) Get the PDO::PARAM_* type for given value
- [`execute(array $options = array()): \PDOStatement|bool`](method-execute.md) Execute the query with the current database handle
