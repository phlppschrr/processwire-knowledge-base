# $modulesClass->log($str, $options = array()): WireLog

Source: `wire/core/ModulesClass.php`

Save to the modules log

## Usage

~~~~~
// basic usage
$wireLog = $modulesClass->log($str);

// usage with all arguments
$wireLog = $modulesClass->log($str, $options = array());
~~~~~

## Arguments

- `$str` `string` Message to log
- `$options` (optional) `array|string` Specify module name (string) or options array

## Return value

- `WireLog`
