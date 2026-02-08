# Functions::wireEmpty()

Source: `wire/core/Functions.php`

Is the given value empty according to ProcessWire standards?

This works the same as PHP’s empty() function except for the following:

- It returns true for Countable objects that have 0 items.
- It considers whitespace-only strings to be empty.
- It considers WireNull objects (like NullPage or any others) to be empty (3.0.149+).
- It uses the string value of objects that can be typecast strings (3.0.150+).
- You cannot pass it an undefined variable without triggering a PHP warning.

~~~~~
// behavior with Countable objects
$a = new WireArray();
empty($a); // PHP’s function returns false
wireEmpty($a); // PW’s function returns true
$a->add('item');
wireEmpty($a); // returns false, since there is now an item

// behavior with whitespace-only string
$s = '  ';
empty($s); // PHP’s function returns false
wireEmpty($s); // PW’s function returns true

// behavior with undefined variable $v
isset($v); // returns false
empty($v); // returns true
wireEmpty($v); // returns true but with PHP’s warning triggered
~~~~~

@param mixed $value Value to test if empty

@return bool

@since 3.0.143
