# Field::___editable()

Source: `wire/core/Field.php`

Is this field editable?

- To maximize efficiency check that `$field->useRoles` is true before calling this.
- If you have already verified that the page is editable, omit or specify null for $page argument.
- **Please note:** this does not check that the provided $page itself is editable. If you want that
  check, then use `$page->editable($field)` instead.


@param Page|null $page Optionally specify a Page for context

@param User|null $user Optionally specify a different user (default = current user)

@return bool
