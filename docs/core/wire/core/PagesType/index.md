# PagesType

Source: `wire/core/PagesType.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `Countable`


Groups:
Group: [other](group-other.md)

ProcessWire PagesType

Pages Type
Provides an interface to the Pages class but specific to a given page class/type, with predefined parent and template.
This class is primarily used by the core as an alternative to `$pages`, providing an API for other Page types like
`User`, `Role`, `Permission`, and `Language`. The `$users`, `$roles`, `$permissions` and `$languages` API variables
are all instances of `PagesType`. This class is typically not instantiated on its own and instead acts as a base class
which is extended.

Methods:
- [`__construct(ProcessWire $wire, Template|int|string|array $templates = array(), int|Page|array $parents = array())`](method-__construct.md)
- [`new(array $options = []): Page`](method-___new.md) (hookable)
- [`addTemplates(array|int|string $templates)`](method-addtemplates.md)
- [`addParents(array|int|string|Page $parents)`](method-addparents.md)
- [`selectorString(string $selectorString): string`](method-selectorstring.md)
- [`loaded(Page $page)`](method-loaded.md)
- [`getLoadOptions(array $loadOptions = array()): array`](method-getloadoptions.md)
- [`find(string $selectorString, array $options = array()): PageArray`](method-find.md)
- [`findIDs(string $selectorString, array $options = array()): array`](method-findids.md)
- [`get(string|int $selectorString): Page|NullPage|null`](method-get.md)
- [`save(Page $page): bool`](method-___save.md) (hookable)
- [`delete(Page $page, bool $recursive = false): bool`](method-___delete.md) (hookable)
- [`add(string $name): Page|NullPage`](method-___add.md) (hookable)
- [`getTemplate(): Template`](method-gettemplate.md)
- [`getTemplates(): array|Template[]`](method-gettemplates.md)
- [`getParentID(): int`](method-getparentid.md)
- [`getParentIDs(): array`](method-getparentids.md)
- [`getParent(): Page|NullPage`](method-getparent.md)
- [`getParents(): PageArray`](method-getparents.md)
- [`setPageClass(string $class)`](method-setpageclass.md)
- [`getPageClass(): string`](method-getpageclass.md)
- [`count(string $selectorString = '', array $options = array()): int`](method-count.md)
- [`getJoinFieldNames(): array`](method-getjoinfieldnames.md)
- [`saveReady(Page $page)`](method-___saveready.md) (hookable)
- [`saveReady(Page $page): array`](method-___saveready.md) (hookable)
- [`saved(Page $page, array $changes = array(), array $values = array())`](method-___saved.md) (hookable)
- [`added(Page $page)`](method-___added.md) (hookable)
- [`deleteReady(Page $page)`](method-___deleteready.md) (hookable)
- [`deleted(Page $page)`](method-___deleted.md) (hookable)
