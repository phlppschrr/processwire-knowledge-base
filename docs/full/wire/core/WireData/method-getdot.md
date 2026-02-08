# WireData::getDot()

Source: `wire/core/WireData.php`

Get a property via dot syntax: field.subfield.subfield

Some classes descending WireData may choose to add a call to this as part of their
get() method as a syntax convenience.

~~~~~
$value = $item->get("parent.title");
~~~~~


@param string $key Name of property you want to retrieve in "a.b" or "a.b.c" format

@return null|mixed Returns value if found or null if not
