# PagesTrash

Source: `wire/core/PagesTrash.php`

Inherits: `Wire`

ProcessWire Pages Trash

Pages Trash
$pages->trasher
Implements page trash/restore/empty methods for the $pages API variable.

Methods:
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`trash(Page $page, bool $save = true): bool`](method-trash.md) Move a page to the trash
- [`restore(Page $page, bool $save = true): bool`](method-restore.md) Restore a page from the trash back to a non-trash state
- [`getRestoreInfo(Page $page, bool $populateToPage = false): array`](method-getrestoreinfo.md) Get info needed to restore a Page that is in the trash
- [`parseTrashPageName(string $name): array|bool`](method-parsetrashpagename.md) Parse a trashed page name into an array of its components
- [`emptyTrash(array $options = array()): int|array`](method-emptytrash.md) Delete all pages in the trash
- [`emptyTrashPass2(array $options, array &$result): int`](method-emptytrashpass2.md) Secondary pass for trash deletion
- [`getTrashTotal(): int`](method-gettrashtotal.md) Get total number of pages in trash
- [`getTrashPage(): Page`](method-gettrashpage.md) Return the root parent trash page
