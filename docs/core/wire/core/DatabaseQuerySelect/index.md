# DatabaseQuerySelect

Source: `wire/core/DatabaseQuerySelect.php`

Inherits: `DatabaseQuery`


Groups:
Group: [other](group-other.md)

ProcessWire DatabaseQuerySelect

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

Methods:
- [`__construct()`](method-__construct.md)
- [`getQuery()`](method-getquery.md)
- [`orderby(string|array $value, bool $prepend = false): $this`](method-orderby.md)
- [`getQuerySelect(): string`](method-getqueryselect.md)
- [`getQueryGroupby(): string`](method-getquerygroupby.md)
- [`getQueryLimit(): string`](method-getquerylimit.md)
