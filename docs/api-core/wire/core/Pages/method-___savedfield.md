# $pages->savedField(Page $page, Field $field)

Source: `wire/core/Pages.php`

Hook called after Pages::saveField successfully executes

## Usage

~~~~~
// basic usage
$result = $pages->savedField($page, $field);

// usage with all arguments
$result = $pages->savedField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`

## Hooking

- Hookable method name: `savedField`
- Implementation: `___savedField`
- Hook with: `Pages::savedField`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::savedField', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::savedField', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## See Also

- [Pages::savedPageOrField()](method-___savedpageorfield.md)
