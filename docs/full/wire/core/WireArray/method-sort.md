# WireArray::sort()

Source: `wire/core/WireArray.php`

Sort this WireArray by the given properties.

- Sort properties can be given as a string in the format `name, datestamp` or as an array of strings,
  i.e. `["name", "datestamp"]`.

- You may also specify the properties as `property.subproperty`, where property resolves to a Wire derived object
  in each item, and subproperty resolves to a property within that object.

- Prepend or append a minus "-" to reverse the sort (per field).

~~~~~
// Sort newest to oldest
$items->sort("-created");

// Sort by last_name then first_name
$items->sort("last_name, first_name");
~~~~~


@param string|array $properties Field names to sort by (CSV string or array).

@param int|null $flags Optionally specify sort flags (see sortFlags method for details).

@return $this reference to current instance.
