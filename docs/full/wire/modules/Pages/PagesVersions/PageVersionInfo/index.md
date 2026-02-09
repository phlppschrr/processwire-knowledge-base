# PageVersionInfo

Source: `wire/modules/Pages/PagesVersions/PageVersionInfo.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

Page Version Info

For pages that are a version, this class represents the `_version`
property of the page. It is also used as the return value for some
methods in the PagesVersions class to return version information.

Methods:
- [`__construct(array $data = [])`](method-__construct.md)
- [`set(string $key, string|int|Page $value): self`](method-set.md)
- [`get(string $key): mixed|NullPage|Page|User|null`](method-get.md)
- [`getPage(): NullPage|Page`](method-getpage.md)
- [`setPage(Page $page)`](method-setpage.md)
- [`getCreatedUser(): NullPage|User`](method-getcreateduser.md)
- [`getModifiedUser(): NullPage|User`](method-getmodifieduser.md)
- [`__toString(): string`](method-__tostring.md)

Constants:
- [`actionRestore`](const-actionrestore.md)
