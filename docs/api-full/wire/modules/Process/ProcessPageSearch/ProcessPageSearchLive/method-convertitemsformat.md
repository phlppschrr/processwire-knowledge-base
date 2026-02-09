# $processPageSearchLive->convertItemsFormat(array $items): array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Convert items from native live search format (v2) to v1 format

v1 format is used by ProcessWire admin themes.

## Usage

~~~~~
// basic usage
$array = $processPageSearchLive->convertItemsFormat($items);

// usage with all arguments
$array = $processPageSearchLive->convertItemsFormat(array $items);
~~~~~

## Arguments

- `$items` `array`

## Return value

- `array`
