# $pagesEditor->savePageQueryException(Page $page, $query, $exception, array $options): bool

Source: `wire/core/PagesEditor.php`

Handle Exception for savePageQuery()

While setupNew() already attempts to uniqify a page name with an incrementing
number, there is a chance that two processes running at once might end up with
the same number, so we account for the possibility here by re-trying queries
that trigger duplicate-entry exceptions.

Example of actual exception text, for reference:
Integrity constraint violation: 1062 Duplicate entry 'background-3552' for key 'name3894_parent_id'

## Arguments

- Page $page
- \PDOStatement $query
- \PDOException|\Exception $exception
- array $options

## Return value

bool True if it should give $query another shot, false if not
