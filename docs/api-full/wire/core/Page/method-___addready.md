# $page->addReady()

Source: `wire/core/Page.php`

Called when this new Page about to be added and saved to the database

## Example

~~~~~
$wire->addHook('Page::addReady', function($e) {
  $page = $e->object;
  $e->message("Ready to add new $page->template page");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->addReady();
~~~~~

## Hooking

- Hookable method name: `addReady`
- Implementation: `___addReady`
- Hook with: `Page::addReady`

### Hooking Before

~~~~~
$this->addHookBefore('Page::addReady', function(HookEvent $event) {
  $page = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::addReady', function(HookEvent $event) {
  $page = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
