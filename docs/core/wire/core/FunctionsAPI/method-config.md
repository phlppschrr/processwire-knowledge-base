# $functionsAPI->config($key = '', $value = null): Config|mixed

Source: `wire/core/FunctionsAPI.php`

Access a ProcessWire configuration setting ($config API variable as a function)

This function behaves the same as the `$config` API variable, though does support
optional shortcut arguments for getting/setting values.

## Example

~~~~~
$config = config(); // Simply get $config API var
$debug = config()->debug; // Get value of debug
$debug = config('debug'); // Same as above, shortcut syntax
config()->debug = true; // Set value of debug
config('debug', true);  // Same as above, shortcut syntax
~~~~~

## Usage

~~~~~
// basic usage
$config = $functionsAPI->config();

// usage with all arguments
$config = $functionsAPI->config($key = '', $value = null);
~~~~~

## Arguments

- `$key` (optional) `string`
- `$value` (optional) `null`

## Return value

- `Config|mixed`

## See Also

- Config
