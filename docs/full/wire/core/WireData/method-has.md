# $wireData->has($key): bool

Source: `wire/core/WireData.php`

Does this object have the given property?

~~~~~
if($item->has('some_property')) {
  // the item has some_property
}
~~~~~

## Arguments

- string $key Name of property you want to check.

## Return value

bool True if it has the property, false if not.
