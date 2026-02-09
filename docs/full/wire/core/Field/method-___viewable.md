# $field->viewable(?Page $page = null, ?User $user = null): bool

Source: `wire/core/Field.php`

Is this field viewable?


- To maximize efficiency check that `$field->useRoles` is true before calling this.
- If you have already verified that the page is viewable, omit or specify null for $page argument.
- **Please note:** this does not check that the provided $page itself is viewable. If you want that
  check, then use `$page->viewable($field)` instead.

## Usage

~~~~~
// basic usage
$bool = $field->viewable();

// usage with all arguments
$bool = $field->viewable(?Page $page = null, ?User $user = null);
~~~~~

## Hookable

- Hookable method name: `viewable`
- Implementation: `___viewable`
- Hook with: `$field->viewable()`

## Hooking Before

~~~~~
$this->addHookBefore('Field::viewable', function(HookEvent $event) {
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
$this->addHookAfter('Field::viewable', function(HookEvent $event) {
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

- `$page` (optional) `Page|null` Optionally specify a Page for context (i.e. Is field viewable on $page?)
- `$user` (optional) `User|null` Optionally specify a different user for context (default=current user)

## Return value

- `bool` True if viewable, false if not
