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

## Hooking Before

~~~~~
$this->addHookBefore('ProcessPageSearchLive::renderItem', function(HookEvent $event) {
  $processPageSearchLive = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $prefix = $event->arguments(1);
  $class = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $prefix);
  $event->arguments(2, $class);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessPageSearchLive::renderItem', function(HookEvent $event) {
  $processPageSearchLive = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $prefix = $event->arguments(1);
  $class = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `array`
- `$prefix` (optional) `string` For CSS classes, default is "pw-search"
- `$class` (optional) `string` Class name for item, default is "item" which translates to "pw-search-item"

## Return value

- `string` HTML markup
