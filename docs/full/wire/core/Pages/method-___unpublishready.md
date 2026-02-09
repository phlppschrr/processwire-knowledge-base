# $pages->unpublishReady(Page $page)

Source: `wire/core/Pages.php`

Hook called right before a published page is unpublished and saved

## Usage

~~~~~
// basic usage
$result = $pages->unpublishReady($page);

// usage with all arguments
$result = $pages->unpublishReady(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Hooking

- Hookable method name: `unpublishReady`
- Implementation: `___unpublishReady`
- Hook with: `Pages::unpublishReady`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::unpublishReady', function(HookEvent $event) {
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
$this->addHookAfter('Pages::unpublishReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
