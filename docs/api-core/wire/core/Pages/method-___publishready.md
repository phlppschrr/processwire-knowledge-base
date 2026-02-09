# $pages->publishReady(Page $page)

Source: `wire/core/Pages.php`

Hook called right before an unpublished page is published and saved

## Usage

~~~~~
// basic usage
$result = $pages->publishReady($page);

// usage with all arguments
$result = $pages->publishReady(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Hooking

- Hookable method name: `publishReady`
- Implementation: `___publishReady`
- Hook with: `Pages::publishReady`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::publishReady', function(HookEvent $event) {
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
$this->addHookAfter('Pages::publishReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
