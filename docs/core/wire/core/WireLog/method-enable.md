# $wireLog->enable($name): self

Source: `wire/core/WireLog.php`

Enable a previously disabled log

## Usage

~~~~~
// basic usage
$result = $wireLog->enable($name);
~~~~~

## Arguments

- `$name` `string` Log name or specify '*' to reverse a previous disable('*') call.

## Return value

- `self`

## See Also

- [WireLog::disable()](method-disable.md)

## Since

3.0.148
