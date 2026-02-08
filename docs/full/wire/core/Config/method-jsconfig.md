# $config->jsConfig($key = null, $value = null): mixed|null|array|self

Source: `wire/core/Config.php`

Set or retrieve a config value exclusive to Javascript (ProcessWire.config)

Values are set to the Javascript variable `ProcessWire.config[key]`.

Unlike $config->js(), values get or set are exclusive to JS config only.

Values set with this method can be retrieved via $config->js() or $config->jsConfig(),
but they cannot be retrieved from $config->['key'] or $config->get('key').

If setting a new property for the JS config it is recommended that you use this
method rather than $config->js() in ProcessWire 3.0.173+. If backwards compatibility
is needed then you should still use $config->js().

1. Specify a $key and $value to set a JS config value.

2. Specify only a $key and omit the $value in order to retrieve an existing set value.

3. Specify no params to retrieve in array of all existing set values.

~~~~~
// Set a property from PHP
$config->jsConfig('mySettings', [
  'foo' => 'bar',
  'bar' => 123,
]);

// Get a property (from PHP)
$mySettings = $config->jsConfig('mySettings');
~~~~~
~~~~~
// Get a property (from Javascript):
var mySettings = ProcessWire.config.mySettings;
console.log(mySettings.foo);
console.log(mySettings.bar);
~~~~~

## Arguments

- `$key` (optional) `string` Name of property to get or set or omit to return all data
- `$value` (optional) `mixed|null` Specify value to set or omit (null) to get

## Return value

mixed|null|array|self Returns null if $key not found, value when getting, self when setting, or array when getting all

## Since

3.0.173
