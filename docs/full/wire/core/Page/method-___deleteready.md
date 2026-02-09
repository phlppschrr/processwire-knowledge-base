# $page->deleteReady()

Source: `wire/core/Page.php`

Called right before this page is deleted (and before any of its data is touched)

## Example

~~~~~
$wire->addHook('Page::deleteReady', function($e) {
  $page = $e->object;
  $e->warning("Page $page WILL be deleted");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->deleteReady();
~~~~~

## Hooking

- Hookable method name: `deleteReady`
- Implementation: `___deleteReady`
- Hook with: `Page::deleteReady`

### Hooking Before

~~~~~
$this->addHookBefore('Page::deleteReady', function(HookEvent $event) {
  $page = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::deleteReady', function(HookEvent $event) {
  $page = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
