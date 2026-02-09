# $pages->trashReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a Page is about to be trashed

## Usage

~~~~~
// basic usage
$result = $pages->trashReady($page);

// usage with all arguments
$result = $pages->trashReady(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Hooking

- Hookable method name: `trashReady`
- Implementation: `___trashReady`
- Hook with: `Pages::trashReady`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::trashReady', function(HookEvent $event) {
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
$this->addHookAfter('Pages::trashReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.163
