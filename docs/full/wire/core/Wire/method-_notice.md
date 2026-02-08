# $wire->_notice($text, $flags, $name, $class): $this

Source: `wire/core/Wire.php`

Record a Notice, internal use (contains the code for message, warning and error methods)

## Usage

~~~~~
// basic usage
$result = $wire->_notice($text, $flags, $name, $class);
~~~~~

## Arguments

- `$text` `string|array|Wire` Title of notice
- `$flags` `int|string` Flags bitmask or space separated string of flag names
- `$name` `string` Name of container
- `$class` `string` Name of Notice class

## Return value

- `$this`
