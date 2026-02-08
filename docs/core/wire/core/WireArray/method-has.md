# $wireArray->has($key): bool

Source: `wire/core/WireArray.php`

Does this WireArray have the given item, index, or match the given selector?

If the WireArray uses numeric keys, then this will also match a WireData object's "name" field.

## Example

~~~~~
// See if it has a given $item
if($items->has($item)) {
  // Has the given $item
}

// See if it has an object with a "name" property matching our text
if($items->has("name=something")) {
  // Has an item with a "name" property equal to "something"
}

// Same as above, but works since "name" is assumed for many types
if($items->has("something")) {
  // It has it
}
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wireArray->has($key);
~~~~~

## Arguments

- `$key` `int|string|Wire` Key of item to check or selector.

## Return value

- `bool` True if the item exists, false if not.
