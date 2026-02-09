# $pages->trashed(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page has been moved to the trash

## Usage

~~~~~
// basic usage
$result = $pages->trashed($page);

// usage with all arguments
$result = $pages->trashed(Page $page);
~~~~~

## Arguments

- `$page` `Page` Page that was moved to the trash

## Hooking

- Hookable method name: `trashed`
- Implementation: `___trashed`
- Hook with: `Pages::trashed`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::trashed', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::trashed', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
