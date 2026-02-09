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
- [`set(string $key, string|int|Page $value): self`](method-set.md) Set property
- [`get(string $key): mixed|NullPage|Page|User|null`](method-get.md) Get property
- [`getPage(): NullPage|Page`](method-getpage.md) Get page that this version is for
- [`setPage(Page $page)`](method-setpage.md) Set page that this version is for
- [`getCreatedUser(): NullPage|User`](method-getcreateduser.md) Get user that created this version
- [`getModifiedUser(): NullPage|User`](method-getmodifieduser.md) Get user that last modified this version
- [`__toString(): string`](method-__tostring.md) String value is version number as a string

Constants:
- [`actionRestore = 'restore'`](const-actionrestore.md)
