# $pages->saveFieldReady(Page $page, Field $field)

Source: `wire/core/Pages.php`

Hook called when Pages::saveField is ready to execute

## Usage

~~~~~
// basic usage
$result = $pages->saveFieldReady($page, $field);

// usage with all arguments
$result = $pages->saveFieldReady(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`

## Hooking

- Hookable method name: `saveFieldReady`
- Implementation: `___saveFieldReady`
- Hook with: `Pages::saveFieldReady`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::saveFieldReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::saveFieldReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## See Also

- [Pages::savePageOrFieldReady()](method-___savepageorfieldready.md)
