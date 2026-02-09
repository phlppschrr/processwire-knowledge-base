# $wireDebugInfo->getDebugInfo(Wire $obj, $small = false): array

Source: `wire/core/WireDebugInfo.php`

Get all debug info for the given Wire object

## Usage

~~~~~
// basic usage
$array = $wireDebugInfo->getDebugInfo($obj);

// usage with all arguments
$array = $wireDebugInfo->getDebugInfo(Wire $obj, $small = false);
~~~~~

## Arguments

- `$obj` `Wire`
- `$small` (optional) `bool` Return non-verbose debug info? (default=false)

## Return value

- `array`
