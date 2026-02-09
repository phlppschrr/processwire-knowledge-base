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

## Hooking Before

~~~~~
$this->addHookBefore('ProcessPageSearchLive::renderList', function(HookEvent $event) {
  $processPageSearchLive = $event->object;

  // Get arguments
  $items = $event->arguments(0);
  $prefix = $event->arguments(1);
  $class = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $items);
  $event->arguments(1, $prefix);
  $event->arguments(2, $class);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessPageSearchLive::renderList', function(HookEvent $event) {
  $processPageSearchLive = $event->object;

  // Get arguments
  $items = $event->arguments(0);
  $prefix = $event->arguments(1);
  $class = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$items` `array`
- `$prefix` (optional) `string` For CSS classes, default is "pw-search"
- `$class` (optional) `string` Class name for list, default is "list" which translates to "pw-search-list"

## Return value

- `string` HTML markup
