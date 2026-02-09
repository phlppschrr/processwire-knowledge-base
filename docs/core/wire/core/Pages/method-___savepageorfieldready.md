# $pages->savePageOrFieldReady(Page $page, $fieldName = '')

Source: `wire/core/Pages.php`

Hook called when either of Pages::save or Pages::saveField is ready to execute

## Usage

~~~~~
// basic usage
$result = $pages->savePageOrFieldReady($page);

// usage with all arguments
$result = $pages->savePageOrFieldReady(Page $page, $fieldName = '');
~~~~~

## Arguments

- `$page` `Page`
- `$fieldName` (optional) `string` Populated only if call originates from saveField

## Hooking

- Hookable method name: `savePageOrFieldReady`
- Implementation: `___savePageOrFieldReady`
- Hook with: `Pages::savePageOrFieldReady`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::savePageOrFieldReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $fieldName = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $fieldName);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::savePageOrFieldReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $fieldName = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## See Also

- [Pages::saveReady()](method-___saveready.md)
- [Pages::saveFieldReady()](method-___savefieldready.md)
