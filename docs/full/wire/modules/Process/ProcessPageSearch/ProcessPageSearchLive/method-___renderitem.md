# $processPageSearchLive->renderItem(array $item, $prefix = 'pw-search', $class = 'item'): string

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Render an item for the “view all” list

## Usage

~~~~~
// basic usage
$string = $processPageSearchLive->renderItem($item);

// usage with all arguments
$string = $processPageSearchLive->renderItem(array $item, $prefix = 'pw-search', $class = 'item');
~~~~~

## Hookable

- Hookable method name: `renderItem`
- Implementation: `___renderItem`
- Hook with: `$processPageSearchLive->renderItem()`

## Arguments

- `$item` `array`
- `$prefix` (optional) `string` For CSS classes, default is "pw-search"
- `$class` (optional) `string` Class name for item, default is "item" which translates to "pw-search-item"

## Return value

- `string` HTML markup
