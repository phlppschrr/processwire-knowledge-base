# $wire->_notice($text, $flags, $name, $class): $this

Source: `wire/core/Wire.php`

Record a Notice, internal use (contains the code for message, warning and error methods)

## Arguments

- string|array|Wire $text Title of notice
- int|string $flags Flags bitmask or space separated string of flag names
- string $name Name of container
- string $class Name of Notice class

## Return value

$this
