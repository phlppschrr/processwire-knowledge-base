# $wireProfilerInterface->start($name, $source = null, $data = array()): mixed

Source: `wire/core/Interfaces.php`

Start profiling an event

Return the event array to be used for stop profiling

## Usage

~~~~~
// basic usage
$result = $wireProfilerInterface->start($name);

// usage with all arguments
$result = $wireProfilerInterface->start($name, $source = null, $data = array());
~~~~~

## Arguments

- `$name` `string` Name of event in format "method" or "method.id" or "something"
- Wire|object|string|null Source of event (may be object instance)
- `$data` (optional) `array`

## Return value

- `mixed` Event to be used for stop call
