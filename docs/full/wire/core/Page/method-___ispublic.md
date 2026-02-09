# $page->isPublic(): bool

Source: `wire/core/Page.php`

Hookable implementation for the above isPublic function

## Usage

~~~~~
// basic usage
$bool = $page->isPublic();
~~~~~

## Return value

- `bool`

## Hooking

- Hookable method name: `isPublic`
- Implementation: `___isPublic`
- Hook with: `Page::isPublic`

### Hooking Before

~~~~~
$this->addHookBefore('Page::isPublic', function(HookEvent $event) {
  $page = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::isPublic', function(HookEvent $event) {
  $page = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
