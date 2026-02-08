# Wire::_notice()

Source: `wire/core/Wire.php`

Record a Notice, internal use (contains the code for message, warning and error methods)

@param string|array|Wire $text Title of notice

@param int|string $flags Flags bitmask or space separated string of flag names

@param string $name Name of container

@param string $class Name of Notice class

@return $this
