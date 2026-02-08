# $functionsWireAPI->wireConfig($key = '', $value = null): Config|mixed

Source: `wire/core/FunctionsWireAPI.php`

Access the $config API variable as a function

## Example

~~~~~
$config = config(); // Simply get $config API var
$debug = config()->debug; // Get value of debug
$debug = config('debug'); // Same as above
config()->debug = true; // Set value of debug
config('debug', true);  // Same as above
~~~~~

## Usage

~~~~~
// basic usage
$config = $functionsWireAPI->wireConfig();

// usage with all arguments
$config = $functionsWireAPI->wireConfig($key = '', $value = null);
~~~~~

## Arguments

- `$key` (optional) `string`
- `$value` (optional) `null`

## Return value

- `Config|mixed`
