# $processPageSearchLive->init(array $presets = array()): array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Initialize live search

## Usage

~~~~~
// basic usage
$array = $processPageSearchLive->init();

// usage with all arguments
$array = $processPageSearchLive->init(array $presets = array());
~~~~~

## Arguments

- `$presets` (optional) `array` Additional info to populate in liveSearchInfo

## Return value

- `array` Current liveSearchInfo
