# WireData::set()

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


@param string $key Name of property you want to set

@param mixed $value Value of property

@return $this

@see WireData::setQuietly(), WireData::get()
