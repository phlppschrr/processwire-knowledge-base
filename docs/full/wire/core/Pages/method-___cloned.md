# $pages->cloned(Page $page, Page $copy)

Source: `wire/core/Pages.php`

Hook called when a page has been cloned

## Usage

~~~~~
// basic usage
$result = $pages->cloned($page, $copy);

// usage with all arguments
$result = $pages->cloned(Page $page, Page $copy);
~~~~~

## Arguments

- `$page` `Page` The original page to be cloned
- `$copy` `Page` The completed cloned version of the page

## Hooking

- Hookable method name: `cloned`
- Implementation: `___cloned`
- Hook with: `Pages::cloned`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::cloned', function(HookEvent $event) {
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
$this->addHookAfter('Pages::cloned', function(HookEvent $event) {
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
