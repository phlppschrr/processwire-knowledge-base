# $pagesEditor->savePageFinish(Page $page, $isNew, array $options): bool

Source: `wire/core/PagesEditor.php`

Save individual Page fields and supporting actions

triggers hooks: saved, added, moved, renamed, templateChanged

## Arguments

- Page $page
- bool $isNew
- array $options

## Return value

bool

## Throws

- \Exception|WireException|\PDOException If any field-saving failure occurs while in a DB transaction
