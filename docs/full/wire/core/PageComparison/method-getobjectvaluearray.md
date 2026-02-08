# $pageComparison->getObjectValueArray($object, $property = ''): array

Source: `wire/core/PageComparison.php`

Given an object, return the value(s) it represents (optionally from a property in the object)

This method is setup for the matches() method above this. It will go recursive when given a property
that resolves to another object.

## Arguments

- Wire|object $object
- string $property Optional property to pull from object (may also be property.subproperty, and so on)

## Return value

array Always returns an array, which may be empty or populated
