# $page->getUnknown($key): null|mixed

Source: `wire/core/Page.php`

Hookable method called when a request to a field was made that didn't match anything

Hooks that want to inject something here should hook after and modify the $event->return.

## Usage

~~~~~
// basic usage
$page->getUnknown($key);
~~~~~

## Arguments

- `$key` `string` Name of property.

## Return value

- `null|mixed` Returns null if property not known, or a value if it is.

## Hooking

- Hookable method name: `getUnknown`
- Implementation: `___getUnknown`
- Hook with: `Page::getUnknown`

### Hooking Before

~~~~~
$this->addHookBefore('Page::getUnknown', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $key = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $key);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::getUnknown', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $key = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
