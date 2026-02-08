# PageComparison::getObjectValueArray()

Source: `wire/core/PageComparison.php`

Given an object, return the value(s) it represents (optionally from a property in the object)

This method is setup for the matches() method above this. It will go recursive when given a property
that resolves to another object.

@param Wire|object $object

@param string $property Optional property to pull from object (may also be property.subproperty, and so on)

@return array Always returns an array, which may be empty or populated
