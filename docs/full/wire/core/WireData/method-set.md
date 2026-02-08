# $wireData->set($key, $value): $this

Source: `wire/core/WireData.php`

Set a value to this object’s data

~~~~~
// Set a value for a property
$item->set('foo', 'bar');

// Set a property value directly
$item->foo = 'bar';

// Set a property using array access
$item['foo'] = 'bar';
~~~~~

## Arguments

- string $key Name of property you want to set
- mixed $value Value of property

## Return value

$this

## See also

- [WireData::setQuietly()](method-setquietly.md)
- [WireData::get()](method-get.md)
