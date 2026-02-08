# $wireArray->data($key = null, $value = null): WireArray|mixed|array|null

Source: `wire/core/WireArray.php`

Store or retrieve an extra data value in this WireArray

The data() function is exactly the same thing that it is in jQuery: <http://api.jquery.com/data/>.

~~~~~~
// set a data value named 'foo' to value 'bar'
$a->data('foo', 'bar');

// retrieve the previously set data value
$bar = $a->data('foo');

// get all previously set data
$all = $a->data();
~~~~~~

[Introduction of data method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

## Arguments

- `$key` (optional) `string|null|array|bool` Name of data property you want to get or set, or: - Omit to get all data properties. - Specify associative array of [property => value] to set multiple properties. - Specify associative array and boolean TRUE for $value argument to replace all data with the new array given in $key. - Specify regular array of property names to return multiple properties. - Specify boolean FALSE to unset property name specified in $value argument.
- `$value` (optional) `mixed|null|bool` Value of data property you want to set. Omit when getting properties. - Specify boolean TRUE to replace all data with associative array of data given in $key argument.

## Return value

WireArray|mixed|array|null Returns one of the following, depending on specified arguments: - `mixed` when getting a single property: whatever you set is what you will get back. - `null` if the property you are trying to get does not exist in the data. - `$this` reference to this WireArray if you were setting a value. - `array` of all data if you specified no arguments or requested multiple keys.
