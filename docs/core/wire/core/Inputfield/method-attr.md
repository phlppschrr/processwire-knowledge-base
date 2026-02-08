# $inputfield->attr($key, $value = null): Inputfield|array|string|int|object|float

Source: `wire/core/Inputfield.php`

Get or set an attribute (or multiple attributes)

- To get an attribute call this method with just the attribute name.
- To set an attribute call this method with the attribute name and value to set.
- You can also set multiple attributes at once, see examples below.
- To get all attributes, just specify boolean true as first argument (since 3.0.16).

~~~~~
// Get the "value" attribute
$value = $inputfield->attr('value');

// Set the "value" attribute
$inputfield->attr('value', 'Foo and Bar');

// Set multiple attributes
$inputfield->attr([
  'name' => 'foobar',
  'value' => 'Foo and Bar',
  'class' => 'foo-bar',
]);

// Set name and id attribute to "foobar"
$inputfield->attr("name+id", "foobar");

// Get all attributes in associative array (since 3.0.16)
$attrs = $inputfield->attr(true);
~~~~~

## Arguments

- string|array|bool $key Specify one of the following: - Name of attribute to get (if getting an attribute). - Name of attribute to set (if setting an attribute, and also specifying a value). - Aassociative array to set multiple attributes. - String with attributes split by "+" or "|" to set them all to have the same value. - Specify boolean true to get all attributes in an associative array.
- string|int|bool|null $value Value to set (if setting), omit otherwise.

## Return value

Inputfield|array|string|int|object|float If setting an attribute, it returns this instance. If getting an attribute, the attribute is returned.

## See also

- [Inputfield::removeAttr()](method-removeattr.md)
- [Inputfield::addClass()](method-addclass.md)
- [Inputfield::removeClass()](method-removeclass.md)
