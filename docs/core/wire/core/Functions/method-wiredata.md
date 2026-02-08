# $functions->WireData($data = array()): WireData

Source: `wire/core/Functions.php`

Create a new WireData instance and optionally add given associative array of data to it

~~~~~
$data = WireData([ 'hello' => 'world', 'foo' => 'bar' ]);
~~~~~

## Arguments

- `$data` (optional) `array|\Traversable` Can be an associative array or Traversable object of data to set, or omit if not needed

## Return value

WireData

## Since

3.0.126
