# $databaseQuery->__call($method, $arguments): $this

Source: `wire/core/DatabaseQuery.php`

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

## Arguments

- `$method` `string`
- `$arguments` `array`

## Return value

$this
