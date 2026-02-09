# PagesTrash

Source: `wire/core/PagesTrash.php`

Inherits: `Wire`

ProcessWire Pages Trash

Pages Trash
$pages->trasher
Implements page trash/restore/empty methods for the $pages API variable.

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`trash(Page $page, bool $save = true): bool`](method-trash.md)
- [`restore(Page $page, bool $save = true): bool`](method-restore.md)
- [`getRestoreInfo(Page $page, bool $populateToPage = false): array`](method-getrestoreinfo.md)
- [`parseTrashPageName(string $name): array|bool`](method-parsetrashpagename.md)
- [`emptyTrash(array $options = array()): int|array`](method-emptytrash.md)
- [`emptyTrashPass2(array $options, array &$result): int`](method-emptytrashpass2.md)
- [`getTrashTotal(): int`](method-gettrashtotal.md)
- [`getTrashPage(): Page`](method-gettrashpage.md)
