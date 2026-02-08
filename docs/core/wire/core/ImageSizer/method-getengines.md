# $imageSizer->getEngines($forceReload = false): array

Source: `wire/core/ImageSizer.php`

Get array of all available ImageSizer engine names in order of priority

Note that the returned value excludes the default engine (ImageSizerEngineGD).

## Usage

~~~~~
// basic usage
$array = $imageSizer->getEngines();

// usage with all arguments
$array = $imageSizer->getEngines($forceReload = false);
~~~~~

## Arguments

- `$forceReload` (optional) `bool` Specify true only if you want to prevent it from using cached result from previous call.

## Return value

- `array` of module names
