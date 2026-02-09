# $page->loaded()

Source: `wire/core/Page.php`

Called when this page has been loaded and is now ready and use

## Example

~~~~~
$wire->addHook('Page::loaded', function($e) {
  $e->message("Loaded page $e->object");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->loaded();
~~~~~

## Hooking

- Hookable method name: `loaded`
- Implementation: `___loaded`
- Hook with: `Page::loaded`

### Hooking Before

~~~~~
$this->addHookBefore('Page::loaded', function(HookEvent $event) {
  $page = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::loaded', function(HookEvent $event) {
  $page = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
