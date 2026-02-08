# $processPageSearchLive->___renderList(array $items, $prefix = 'pw-search', $class = 'list'): string

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Render “view all” list

## Usage

~~~~~
// basic usage
$string = $processPageSearchLive->___renderList($items);

// usage with all arguments
$string = $processPageSearchLive->___renderList(array $items, $prefix = 'pw-search', $class = 'list');
~~~~~

## Arguments

- `$items` `array`
- `$prefix` (optional) `string` For CSS classes, default is "pw-search"
- `$class` (optional) `string` Class name for list, default is "list" which translates to "pw-search-list"

## Return value

- `string` HTML markup
