# $processPageSearchLive->makeViewAllItem(&$liveSearch, $type, $group, $total, $url = ''): array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Make a search result item that displays a “view all” link

## Usage

~~~~~
// basic usage
$array = $processPageSearchLive->makeViewAllItem($liveSearch, $type, $group, $total);

// usage with all arguments
$array = $processPageSearchLive->makeViewAllItem(&$liveSearch, $type, $group, $total, $url = '');
~~~~~

## Arguments

- `$liveSearch` `array`
- `$type` `string`
- `$group` `string`
- `$total` `int`
- `$url` (optional) `string` If module provides its own view-all URL

## Return value

- `array`
