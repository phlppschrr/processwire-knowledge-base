# $field->___viewable(?Page $page = null, ?User $user = null): bool

Source: `wire/core/Field.php`

Is this field viewable?


- To maximize efficiency check that `$field->useRoles` is true before calling this.
- If you have already verified that the page is viewable, omit or specify null for $page argument.
- **Please note:** this does not check that the provided $page itself is viewable. If you want that
  check, then use `$page->viewable($field)` instead.

## Arguments

- Page|null $page Optionally specify a Page for context (i.e. Is field viewable on $page?)
- User|null $user Optionally specify a different user for context (default=current user)

## Return value

bool True if viewable, false if not
