# $processPageSearchLive->makeHelpItems(array $result, $type): array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Make a search result item that displays property info

## Usage

~~~~~
// basic usage
$array = $processPageSearchLive->makeHelpItems($result, $type);

// usage with all arguments
$array = $processPageSearchLive->makeHelpItems(array $result, $type);
~~~~~

## Arguments

- `$result` `array` Result array returned by a SearchableModule::search() method
- `$type` `string`

## Return value

- `array`
