# WireData::has()

Source: `wire/core/WireData.php`

Does this object have the given property?

~~~~~
if($item->has('some_property')) {
  // the item has some_property
}
~~~~~


@param string $key Name of property you want to check.

@return bool True if it has the property, false if not.
