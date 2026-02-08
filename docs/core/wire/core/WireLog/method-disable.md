# $wireLog->disable($name): self

Source: `wire/core/WireLog.php`

Disable the given log name temporarily so that save() calls do not record entries during this request

## Usage

~~~~~
// basic usage
$result = $wireLog->disable($name);
~~~~~

## Arguments

- `$name` `string` Log name or specify '*' to disable all

## Return value

- `self`

## See Also

- [WireLog::enable()](method-enable.md)

## Since

3.0.148
