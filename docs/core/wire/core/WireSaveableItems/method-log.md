# $wireSaveableItems->log($str, ?Saveable $item = null): WireLog

Source: `wire/core/WireSaveableItems.php`

Save to activity log, if enabled in config

## Usage

~~~~~
// basic usage
$wireLog = $wireSaveableItems->log($str);

// usage with all arguments
$wireLog = $wireSaveableItems->log($str, ?Saveable $item = null);
~~~~~

## Arguments

- $str
- Saveable|null Item to log

## Return value

- `WireLog`
