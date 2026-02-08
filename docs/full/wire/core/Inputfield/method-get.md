# $inputfield->get($key): mixed|null

Source: `wire/core/Inputfield.php`

Get a property or attribute from the Inputfield

- This can also be accessed directly, i.e. `$value = $inputfield->property;`.

- For getting attribute values, this will work, but it is preferable to use the `Inputfield::attr()` method.

- For getting non-attribute values that have potential name conflicts with attributes (or just as a
  reliable alternative), use the `Inputfield::getSetting()` method instead, which excludes the possibility
  of overlap with attributes.

## Arguments

- string $key Name of property or attribute to retrieve.

## Return value

mixed|null Value of property or attribute, or NULL if not found.
