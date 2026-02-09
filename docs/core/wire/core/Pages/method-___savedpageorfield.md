# $pages->savedPageOrField(Page $page, array $changes = array())

Source: `wire/core/Pages.php`

Hook called after either of Pages::save or Pages::saveField successfully executes

## Usage

~~~~~
// basic usage
$result = $pages->savedPageOrField($page);

// usage with all arguments
$result = $pages->savedPageOrField(Page $page, array $changes = array());
~~~~~

## Hookable

- Hookable method name: `savedPageOrField`
- Implementation: `___savedPageOrField`
- Hook with: `$pages->savedPageOrField()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::savedPageOrField', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $changes = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $changes);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::savedPageOrField', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $changes = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page`
- `$changes` (optional) `array` Names of fields

## See Also

- [Pages::saved()](method-___saved.md)
- [Pages::savedField()](method-___savedfield.md)
