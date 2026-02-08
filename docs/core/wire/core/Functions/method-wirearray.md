# Functions::WireArray()

Source: `wire/core/Functions.php`

Create new WireArray, add given $items to it, and return it

This is the same as creating a `new WireArray()` and then adding items to it with separate `add()` calls,
except that this function enables you to do it all in one shot.

~~~~~~
$a = WireArray(); // create empty WireArray
$a = WireArray('foo'); // create WireArray with one "foo" string
$a = WireArray(['foo', 'bar', 'baz']); // create WireArray with 3 strings
~~~~~~


@param array|WireArray|mixed $items

@return WireArray

@since 3.0.123
