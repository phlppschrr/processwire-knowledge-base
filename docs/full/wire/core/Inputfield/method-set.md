# $inputfield->set($key, $value): Inputfield|WireData

Source: `wire/core/Inputfield.php`

Set a property or attribute to the Inputfield

- Use this for setting properties like parent, collapsed, required, columnWidth, etc.
- You can also set properties directly via `$inputfield->property = $value`.
- If setting an attribute (like name, id, etc.) this will work, but it is preferable to use the `Inputfield::attr()` method.
- If setting any kind of "class" it is preferable to use the `Inputfield::addClass()` method.

## Usage

~~~~~
// basic usage
$inputfield = $inputfield->set($key, $value);
~~~~~

## Arguments

- `$key` `string` Name of property to set
- `$value` `mixed` Value of property

## Return value

- `Inputfield|WireData`
