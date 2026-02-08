# $processPageSearchLive->renderList(array $items, $prefix = 'pw-search', $class = 'list'): string

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Render “view all” list

## Usage

~~~~~
// basic usage
$string = $processPageSearchLive->renderList($items);

// usage with all arguments
$string = $processPageSearchLive->renderList(array $items, $prefix = 'pw-search', $class = 'list');
~~~~~

## Hookable

- Hookable method name: `renderList`
- Implementation: `___renderList`
- Hook with: `$processPageSearchLive->renderList()`

## Arguments

- `$items` `array`
- `$prefix` (optional) `string` For CSS classes, default is "pw-search"
- `$class` (optional) `string` Class name for list, default is "list" which translates to "pw-search-list"

## Return value

- `string` HTML markup
