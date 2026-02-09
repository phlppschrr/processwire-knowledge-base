# $page->removeStatusReady($name, $value)

Source: `wire/core/Page.php`

Called when status flag is about to removed from page but not yet saved

## Example

~~~~~
$wire->addHook('Page::removeStatusReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  if($name === 'hidden' && $page->template->name === 'sitemap') {
    $page->addStatus($name);
    $e->error("Sitemap must remain hidden");
  }
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->removeStatusReady($name, $value);
~~~~~

## Arguments

- `$name` `string` Name of the status flag to be removed, i.e. unpublished, hidden, trash, locked
- `$value` `int` Value of the status flag to be removed, a `Page::status*` constant

## Hooking

- Hookable method name: `removeStatusReady`
- Implementation: `___removeStatusReady`
- Hook with: `Page::removeStatusReady`

### Hooking Before

~~~~~
$this->addHookBefore('Page::removeStatusReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $value = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $value);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::removeStatusReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $value = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
