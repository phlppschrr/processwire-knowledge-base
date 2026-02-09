# $pages->delete(Page $page, $recursive = false, array $options = array()): bool|int

Source: `wire/core/Pages.php`

Permanently delete a page, its fields and assets.

Unlike trash(), pages deleted here are not restorable. If you attempt to delete a page with children,
and don't specifically set the `$recursive` argument to `true`, then this method will throw an exception.
If a recursive delete fails for any reason, an exception will also will be thrown.

## Example

~~~~~
// Delete a product page
$product = $pages->get('/products/foo-bar-widget/');
$pages->delete($product);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $pages->delete($page);

// usage with all arguments
$bool = $pages->delete(Page $page, $recursive = false, array $options = array());
~~~~~

## Arguments

- `$page` `Page` Page to delete
- `$recursive` (optional) `bool|array` If set to true, then this will attempt to delete all children too. If you don't need this argument, optionally provide $options array instead.
- `$options` (optional) `array` Optional settings to change behavior: - uncacheAll (bool): Whether to clear memory cache after delete (default=false) - recursive (bool): Same as $recursive argument, may be specified in $options array if preferred.

## Return value

- `bool|int` Returns true (success), or integer of quantity deleted if recursive mode requested.

## Hooking

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `Pages::delete`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::delete', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $recursive = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $recursive);
  $event->arguments(2, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::delete', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $recursive = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` on fatal error

## See Also

- [Pages::trash()](method-___trash.md)
