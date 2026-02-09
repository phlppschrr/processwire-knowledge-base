# $wireData->set($key, $value): $this

Source: `wire/core/WireData.php`

Set a value to this object’s data

## Example

~~~~~
// Set a value for a property
$item->set('foo', 'bar');

// Set a property value directly
$item->foo = 'bar';

// Set a property using array access
$item['foo'] = 'bar';
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireData->set($key, $value);
~~~~~

## Arguments

- `$key` `string` Name of property you want to set
- `$value` `mixed` Value of property

## Return value

- `$this`

## See Also

- [WireData::setQuietly()](method-setquietly.md)
- [WireData::get()](method-get.md)
