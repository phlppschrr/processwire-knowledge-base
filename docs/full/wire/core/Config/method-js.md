# $config->js($key = null, $value = null): array|mixed|null|$this

Source: `wire/core/Config.php`

Set or retrieve a config value to be shared with javascript

Values are set to the Javascript variable `ProcessWire.config[key]`.

Note: In ProcessWire 3.0.173+ when setting new values, it is preferable to use
$config->jsConfig() instead, unless your intended use is to share an
existing $config property with JS.

1. Specify a $key and $value to set a JS config value.

2. Specify only a $key and omit the $value in order to retrieve an existing set value.
   The $key may also be an array of properties, which will return an array of values.

3. Specify boolean true for $value to share the $key with the JS side. If the $key
   specified does not exist then $key=true will be added to the JS config (which can later
   be overwritten with another value, which will still be shared with the JS config).
   The $key property may also be an array of properties to specify multiple.

4. Specify no params to retrieve in array of all existing set values.

~~~~~
// Set a property from PHP
$config->js('mySettings', [
  'foo' => 'bar',
  'bar' => 123,
]);

// Get a property (from PHP)
$mySettings = $config->js('mySettings');
~~~~~
~~~~~
// Get a property (from Javascript):
var mySettings = ProcessWire.config.mySettings;
console.log(mySettings.foo);
console.log(mySettings.bar);
~~~~~

## Arguments

- `$key` (optional) `string|array` Property or array of properties
- `$value` (optional) `mixed`

## Return value

array|mixed|null|$this
