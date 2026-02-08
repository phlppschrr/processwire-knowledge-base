# $functionsWireAPI->wireConfig($key = '', $value = null): Config|mixed

Source: `wire/core/FunctionsWireAPI.php`

Access the $config API variable as a function

~~~~~
$config = config(); // Simply get $config API var
$debug = config()->debug; // Get value of debug
$debug = config('debug'); // Same as above
config()->debug = true; // Set value of debug
config('debug', true);  // Same as above
~~~~~

## Arguments

- string $key
- null $value

## Return value

Config|mixed
