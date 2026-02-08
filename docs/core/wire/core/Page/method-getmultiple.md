# $page->getMultiple($keys, $assoc = false): array

Source: `wire/core/Page.php`

Get multiple Page property/field values in an array

This method works exactly the same as the `get()` method except that it accepts an
array (or CSV string) of properties/fields to get, and likewise returns an array
of those property/field values. By default it returns a regular (non-indexed) PHP
array in the same order given. To instead get an associative array indexed by the
property/field names given, specify `true` for the `$assoc` argument.

~~~~~
// returns regular array i.e. [ 'foo val', 'bar val' ]
$a = $page->getMultiple([ 'foo', 'bar' ]);
list($foo, $bar) = $a;

// returns associative array i.e. [ 'foo' => 'foo val', 'bar' => 'bar val' ]
$a = $page->getMultiple([ 'foo', 'bar' ], true);
$foo = $a['foo'];
$bar = $a['bar'];

// CSV string can also be used instead of array
$a = $page->getMultiple('foo,bar');
~~~~~

## Arguments

- array|string $keys Array or CSV string of properties to get.
- bool $assoc Get associative array indexed by given properties? (default=false)

## Return value

array

## Meta

- @since 3.0.201
