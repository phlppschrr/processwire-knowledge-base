# $pages->published(Page $page)

Source: `wire/core/Pages.php`

Hook called after an unpublished page has just been published

## Usage

~~~~~
// basic usage
$result = $pages->published($page);

// usage with all arguments
$result = $pages->published(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Hooking

- Hookable method name: `published`
- Implementation: `___published`
- Hook with: `Pages::published`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::published', function(HookEvent $event) {
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
$this->addHookAfter('Pages::published', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
