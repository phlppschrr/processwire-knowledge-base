# $pages->unpublished(Page $page)

Source: `wire/core/Pages.php`

Hook called after published page has just been unpublished

## Usage

~~~~~
// basic usage
$result = $pages->unpublished($page);

// usage with all arguments
$result = $pages->unpublished(Page $page);
~~~~~

## Hookable

- Hookable method name: `unpublished`
- Implementation: `___unpublished`
- Hook with: `$pages->unpublished()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::unpublished', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::unpublished', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page`
