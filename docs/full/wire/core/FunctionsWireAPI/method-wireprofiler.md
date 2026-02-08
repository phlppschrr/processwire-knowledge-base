# $functionsWireAPI->wireProfiler($name = null, $source = null, $data = array()): null|array|object

Source: `wire/core/FunctionsWireAPI.php`

Start or stop a profiler event or return WireProfilerInterface instance

## Usage

~~~~~
// basic usage
$functionsWireAPI->wireProfiler();

// usage with all arguments
$functionsWireAPI->wireProfiler($name = null, $source = null, $data = array());
~~~~~

## Arguments

- `$name` (optional) `string|array|object|null` Name of event to start or event to stop
- `$source` (optional) `null|object|string` If starting an event, optional source of event (object)
- `$data` (optional) `array` Optional extra data as associative array

## Return value

- `null|array|object`
