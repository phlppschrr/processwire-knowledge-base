# $field->editable(?Page $page = null, ?User $user = null): bool

Source: `wire/core/Field.php`

Is this field editable?

- To maximize efficiency check that `$field->useRoles` is true before calling this.
- If you have already verified that the page is editable, omit or specify null for $page argument.
- **Please note:** this does not check that the provided $page itself is editable. If you want that
  check, then use `$page->editable($field)` instead.

## Usage

~~~~~
// basic usage
$bool = $field->editable();

// usage with all arguments
$bool = $field->editable(?Page $page = null, ?User $user = null);
~~~~~

## Hookable

- Hookable method name: `editable`
- Implementation: `___editable`
- Hook with: `$field->editable()`

## Hooking Before

~~~~~
$this->addHookBefore('Field::editable', function(HookEvent $event) {
  $field = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $user = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $user);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Field::editable', function(HookEvent $event) {
  $field = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $user = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` (optional) `Page|null` Optionally specify a Page for context
- `$user` (optional) `User|null` Optionally specify a different user (default = current user)

## Return value

- `bool`
