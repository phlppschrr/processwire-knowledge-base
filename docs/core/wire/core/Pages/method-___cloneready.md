# $pages->cloneReady(Page $page, Page $copy)

Source: `wire/core/Pages.php`

Hook called when a page is about to be cloned, but before data has been touched

## Usage

~~~~~
// basic usage
$result = $pages->cloneReady($page, $copy);

// usage with all arguments
$result = $pages->cloneReady(Page $page, Page $copy);
~~~~~

## Arguments

- `$page` `Page` The original page to be cloned
- `$copy` `Page` The actual clone about to be saved

## Hooking

- Hookable method name: `cloneReady`
- Implementation: `___cloneReady`
- Hook with: `Pages::cloneReady`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::cloneReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $copy = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $copy);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::cloneReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $copy = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
