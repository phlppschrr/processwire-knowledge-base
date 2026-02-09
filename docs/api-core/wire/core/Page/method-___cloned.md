# $page->cloned(Page $copy)

Source: `wire/core/Page.php`

Called right after this page has been cloned

## Example

~~~~~
$wire->addHook('Page::cloned', function($e) {
  $page = $e->object;
  $copy = $e->arguments(1);
  $e->log->message("Page $page has been closed to page $copy");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->cloned($copy);

// usage with all arguments
$result = $page->cloned(Page $copy);
~~~~~

## Arguments

- `$copy` `Page` The new cloned copy of the page

## Hooking

- Hookable method name: `cloned`
- Implementation: `___cloned`
- Hook with: `Page::cloned`

### Hooking Before

~~~~~
$this->addHookBefore('Page::cloned', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $copy = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $copy);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::cloned', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $copy = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
