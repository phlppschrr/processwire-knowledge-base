# FunctionsWireAPI::wireConfig()

Source: `wire/core/FunctionsWireAPI.php`

Access the $config API variable as a function

~~~~~
$config = config(); // Simply get $config API var
$debug = config()->debug; // Get value of debug
$debug = config('debug'); // Same as above
config()->debug = true; // Set value of debug
config('debug', true);  // Same as above
~~~~~

@param string $key

@param null $value

@return Config|mixed
