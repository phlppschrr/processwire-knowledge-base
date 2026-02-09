# $page->saved(array $changes, $name = false)

Source: `wire/core/Page.php`

Called right after this Page is saved

Note that if the `$name` argument is populated then only that field/property was saved.
This is different from the `Pages::saved` hookable method, which is only called
when the entire page is saved.

## Example

~~~~~
$wire->addHook('Page:saved', function($e) {
  $page = $e->object;
  $changes = $e->arguments(0);
  $name = $e->arguments(1);
  if($name) {
    $e->message("Saved field $name on page $page");
  } else {
    $e->message("Saved page $page: " . implode(', ', $changes));
  }
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->saved($changes);

// usage with all arguments
$result = $page->saved(array $changes, $name = false);
~~~~~

## Arguments

- `$changes` `array` Names of changed field names and/or properties
- `$name` (optional) `string|false` Indicates whether entire page was saved or just a field: - Populated with `string` field or property name if `$page->save($name)` was used rather than `$page->save();` - Populated with `false` if entire page was saved, i.e. `$page->save()`

## Hooking

- Hookable method name: `saved`
- Implementation: `___saved`
- Hook with: `Page::saved`

### Hooking Before

~~~~~
$this->addHookBefore('Page::saved', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $changes = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $changes);
  $event->arguments(1, $name);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::saved', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $changes = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
