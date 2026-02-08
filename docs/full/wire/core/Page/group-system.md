# Page: system

Source: `wire/core/Page.php`

Most system properties directly correspond to columns in the `pages` database table.

@property int $id The numbered ID of the current page

@property string $name The name assigned to the page, as it appears in the URL

@property int $parent_id The numbered ID of the parent page or 0 if homepage or not assigned.

@property int $templates_id The numbered ID of the template usedby this page.

@property int $created Unix timestamp of when the page was created.

@property int $modified Unix timestamp of when the page was last modified.

@property int $published Unix timestamp of when the page was published.

@property int $created_users_id ID of created user.

@property int $modified_users_id ID of last modified user.

@property int $sort Sort order of this page relative to siblings (applicable when manual sorting is used).

@property int|null $sortPrevious Previous sort order, if changed (3.0.235+)

@property string $sortfield Field that a page is sorted by relative to its siblings (default="sort", which means drag/drop manual)

@property int $status Page status flags.
