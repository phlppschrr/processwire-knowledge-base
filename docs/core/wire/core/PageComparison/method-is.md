# $pageComparison->is(Page $page, $status): bool

Source: `wire/core/PageComparison.php`

Is this page of the given type? (status, template, etc.)

## Arguments

- Page $page
- int|string|array|Selectors|Page|Template $status One of the following: - Status expressed as int (using Page::status* constants) - Status expressed as string/name, i.e. "hidden" (3.0.150+) - Template name, indicating page type - Page or Template object (3.0.150+) - Selector string or Selectors object that must match - Array of any of the above where all have to match (3.0.150+)

## Return value

bool
