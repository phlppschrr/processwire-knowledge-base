# Page: system

Source: `wire/core/Page.php`

Most system properties directly correspond to columns in the `pages` database table.

- $id: int The numbered ID of the current page
- $name: string The name assigned to the page, as it appears in the URL
- $parent_id: int The numbered ID of the parent page or 0 if homepage or not assigned.
- $templates_id: int The numbered ID of the template usedby this page.
- $created: int Unix timestamp of when the page was created.
- $modified: int Unix timestamp of when the page was last modified.
- $published: int Unix timestamp of when the page was published.
- $created_users_id: int ID of created user.
- $modified_users_id: int ID of last modified user.
- $sort: int Sort order of this page relative to siblings (applicable when manual sorting is used).
- $sortPrevious: int|null Previous sort order, if changed (3.0.235+)
- [$sortfield: string](method-sortfield.md) Field that a page is sorted by relative to its siblings (default="sort", which means drag/drop manual)
- [$status: int](method-status.md) Page status flags.
