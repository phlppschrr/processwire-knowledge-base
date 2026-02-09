# $page->added()

Source: `wire/core/Page.php`

Called after this new Page has been added

## Example

~~~~~
$wire->addHook('Page::added', function($e) {
  $page = $e->object;
  $e->message("Added new $page->template page: $page->path");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->added();
~~~~~

## Hooking

- Hookable method name: `added`
- Implementation: `___added`
- Hook with: `Page::added`

### Hooking Before

~~~~~
$this->addHookBefore('Page::added', function(HookEvent $event) {
  $page = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::added', function(HookEvent $event) {
  $page = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
