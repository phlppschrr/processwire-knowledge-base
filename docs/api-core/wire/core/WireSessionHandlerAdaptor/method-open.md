# $wireSessionHandlerAdaptor->open(string $path, string $name): bool

Source: `wire/core/WireSessionHandlerAdaptor.php`

Re-initialize existing session, or creates a new one.

Called when a session starts or when `session_start()` is invoked.

## Usage

~~~~~
// basic usage
$bool = $wireSessionHandlerAdaptor->open($path, $name);

// usage with all arguments
$bool = $wireSessionHandlerAdaptor->open(string $path, string $name);
~~~~~

## Arguments

- `$path` `string`
- `$name` `string`

## Return value

- `bool`
