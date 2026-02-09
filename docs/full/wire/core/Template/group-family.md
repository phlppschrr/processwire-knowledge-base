# Template: family

Source: `wire/core/Template.php`

- `$sortfield: string` Field that children of templates using this page should sort by (leave blank to let page decide, or specify "sort" for manual drag-n-drop).
- `$noChildren: int` Set to 1 to cancel use of childTemplates.
- `$noParents: int` Set to 1 to cancel use of parentTemplates, set to -1 to only allow one page using this template to exist.
- [`$childTemplates: int[]`](method-childtemplates.md) Array of template IDs that are allowed for children. Blank array indicates "any".
- [`$parentTemplates: int[]`](method-parenttemplates.md) Array of template IDs that are allowed for parents. Blank array indicates "any".
- `$childNameFormat: string` Name format for child pages. when specified, the page-add UI step can be skipped when adding children. Counter appended till unique. Date format assumed if any non-pageName chars present. Use 'title' to pull from title field.
