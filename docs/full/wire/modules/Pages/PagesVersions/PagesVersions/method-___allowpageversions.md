# $pagesVersions->allowPageVersions(Page $page): bool

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Is given page allowed to have versions?

## Usage

~~~~~
// basic usage
$bool = $pagesVersions->allowPageVersions($page);

// usage with all arguments
$bool = $pagesVersions->allowPageVersions(Page $page);
~~~~~

## Hookable

- Hookable method name: `allowPageVersions`
- Implementation: `___allowPageVersions`
- Hook with: `$pagesVersions->allowPageVersions()`

## Arguments

- `$page` `Page`

## Return value

- `bool`
