# DatabaseQuerySelect

Source: `wire/core/DatabaseQuerySelect.php`

Inherits: `DatabaseQuery`

## Summary

ProcessWire DatabaseQuerySelect

Common methods:
- [`getQuery()`](method-getquery.md)
- [`orderby()`](method-orderby.md)
- [`getQuerySelect()`](method-getqueryselect.md)
- [`getQueryGroupby()`](method-getquerygroupby.md)
- [`getQueryLimit()`](method-getquerylimit.md)

Groups:
Group: [other](group-other.md)

A wrapper for SELECT SQL queries.

The intention behind these classes is to have a query that can safely
be passed between methods and objects that add to it without knowledge
of what other methods/objects have done to it. It also means being able
to build a complex query without worrying about correct syntax placement.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/




Below are Properties populated by DatabaseQuerySelect objects created by PageFinder.
This is what gets passed to Fieldtype::getMatchQuery() method calls as properties
available from the $query argument.

## Methods
- [`__construct()`](method-__construct.md) Setup the components of a SELECT query
- [`getQuery()`](method-getquery.md) Return the resulting SQL ready for execution with the database
- [`orderby(string|array $value, bool $prepend = false): $this`](method-orderby.md) Add an ORDER BY section to the query
- [`getQuerySelect(): string`](method-getqueryselect.md) Get SELECT portion of SQL
- [`getQueryGroupby(): string`](method-getquerygroupby.md) Get GROUP BY section of SQL
- [`getQueryLimit(): string`](method-getquerylimit.md) Get LIMIT section of SQL
