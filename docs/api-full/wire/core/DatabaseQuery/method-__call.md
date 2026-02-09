# $databaseQuery->__call($method, $arguments): $this

Source: `wire/core/DatabaseQuery.php`

Enables calling the various parts of a query as functions for a fluent interface.

Examples (all in context of DatabaseQuerySelect):
To bind one or more named parameters, specify associative array as second argument:
To bind one or more implied parameters, use question marks and specify regular array:
When there is only one implied parameter, specifying an array is optional:

The "select" or "where" methods above may be any method supported by the class.
Implied parameters (using "?") was added in 3.0.157.

## Example

~~~~~
$query->select("id")->from("mytable")->orderby("name");
~~~~~

~~~~~
$query->where("name=:name", [ ':name' => $page->name ]);
~~~~~

~~~~~
$query->where("name=?, id=?", [ $page->name, $page->id ]);
~~~~~

~~~~~
$query->where("name=?", $page->name);
~~~~~

## Usage

~~~~~
// basic usage
$result = $databaseQuery->__call($method, $arguments);
~~~~~

## Arguments

- `$method` `string`
- `$arguments` `array`

## Return value

- `$this`
