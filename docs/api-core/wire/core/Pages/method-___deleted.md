# $pages->deleted(Page $page, array $options = array())

Source: `wire/core/Pages.php`

Hook called after a page and its data have been deleted

## Usage

~~~~~
// basic usage
$result = $pages->deleted($page);

// usage with all arguments
$result = $pages->deleted(Page $page, array $options = array());
~~~~~

## Arguments

- `$page` `Page` Page that was deleted
- `$options` (optional) `array` Options passed to delete method (since 3.0.163)

## Hooking

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `Pages::deleted`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::deleted', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::deleted', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
