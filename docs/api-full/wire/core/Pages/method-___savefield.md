# $pages->saveField(Page $page, $field, $options = array()): bool

Source: `wire/core/Pages.php`

Save only a field from the given page

This is the same as calling `$page->save($field)`.

## Example

~~~~~
// Update the summary field on $page and save it
$page->summary = "Those who know do not speak. Those who speak do not know.";
$pages->saveField($page, 'summary');
~~~~~

## Usage

~~~~~
// basic usage
$bool = $pages->saveField($page, $field);

// usage with all arguments
$bool = $pages->saveField(Page $page, $field, $options = array());
~~~~~

## Arguments

- `$page` `Page` Page to save
- `$field` `string|Field` Field object or name (string)
- `$options` (optional) `array|string` Optionally specify one or more of the following to modify default behavior: - `quiet` (boolean): Specify true to bypass updating of modified user and time (default=false). - `noHooks` (boolean): Prevent before/after save hooks (default=false), please also use $pages->___saveField() for call.

## Return value

- `bool` True on success, false on failure

## Hooking

- Hookable method name: `saveField`
- Implementation: `___saveField`
- Hook with: `Pages::saveField`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::saveField', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
  $event->arguments(2, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::saveField', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException`

## See Also

- [Page::save()](../Page/method-save.md)
- [Page::setAndSave()](../Page/method-setandsave.md)
- [Pages::save()](method-___save.md)
