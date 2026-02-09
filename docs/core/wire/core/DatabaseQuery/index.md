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
- [`__construct()`](method-__construct.md)
- [`bindOption(string|bool $optionName, null|int|string|array $optionValue = null): string|int|array`](method-bindoption.md)
- [`bindValue(string $key, mixed $value, $type = null): $this`](method-bindvalue.md)
- [`bindValueGetKey(string|int|float $value, null|int|string $type = null): string`](method-bindvaluegetkey.md)
- [`getUniqueBindKey(array $options = array()): string`](method-getuniquebindkey.md)
- [`getBindValues(string|\PDOStatement|DatabaseQuery|array $options = array()): array|int`](method-getbindvalues.md)
- [`copyBindValuesTo(DatabaseQuery|\PDOStatement $query, array $options = array()): int`](method-copybindvaluesto.md)
- [`copyTo(DatabaseQuery $query, array $methods = array()): int`](method-copyto.md)
- [`__call(string $method, array $arguments): $this`](method-__call.md)
- [`__set(string $key, mixed $value)`](method-__set.md)
- [`__get(string $key): array|mixed|null`](method-__get.md)
- [`getQuery(): string`](method-getquery.md)
- [`getDebugQuery(): string`](method-getdebugquery.md)
- [`getSQL(string $method = ''): string`](method-getsql.md)
- [`getQueryMethod(string $method): string`](method-getquerymethod.md)
- [`prepare()`](method-prepare.md)
- [`prepare(): \PDOStatement`](method-prepare.md)
- [`pdoParamType(string|int|null $value): int`](method-pdoparamtype.md)
- [`execute(array $options = array()): \PDOStatement|bool`](method-execute.md)
