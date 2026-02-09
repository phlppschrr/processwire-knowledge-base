# $wireData->setArray(array $data): $this

Source: `wire/core/WireData.php`

Set an array of key=value pairs

This is the same as the `WireData::set()` method except that it can set an array
of properties at once.

## Usage

~~~~~
// basic usage
$result = $wireData->setArray($data);

// usage with all arguments
$result = $wireData->setArray(array $data);
~~~~~

## Arguments

- `$data` `array` Associative array of where the keys are property names, and values are… values.

## Return value

- `$this`

## See Also

- [WireData::set()](method-set.md)
