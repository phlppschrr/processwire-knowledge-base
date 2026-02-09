# Notice

Source: `wire/core/Notice.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

ProcessWire Notice

Notice
Manages notifications in the ProcessWire admin, primarily for internal use.
Base class that holds a message, source class, and timestamp.
Contains individual notices/messages used by the application to display to the user.
Notice items come in three different classes: NoticeMessage, NoticeWarning and NoticeError.
They are all identical in terms of API, with the only difference being that they render as
informational messages, warnings, or errors.

Methods:
- [`__construct(string $text, int|string|array $flags = 0)`](method-__construct.md) Create the Notice
- [`set(string $key, mixed $value): $this|WireData`](method-set.md) Set property
- [`get(string $key): mixed`](method-get.md) Get property
- [`flags(string|int|array|null $value = null): int`](method-flags.md) Get or set flags
- [`flag(string|int $name): int`](method-flag.md) Given flag name or int, return flag int
- [`flagNames(null|int $flags = null, bool $getString = false): array|string`](method-flagnames.md) Get string of names for given flags integer
- [`addFlag(int|string $flag)`](method-addflag.md) Add a flag
- [`removeFlag(int|string $flag)`](method-removeflag.md) Remove a flag
- [`hasFlag(int|string $flag): bool`](method-hasflag.md) Does this Notice have given flag?
- [`getName(): string`](method-getname.md) Get the name for this type of Notice
- [`viewable(): bool`](method-viewable.md) Is this notice viewable at runtime?

Constants:
- [`prepend`](const-prepend.md)
- [`debug`](const-debug.md)
- [`log`](const-log.md)
- [`logOnly`](const-logonly.md)
- [`allowMarkup`](const-allowmarkup.md)
- [`markup`](const-markup.md)
- [`anonymous`](const-anonymous.md)
- [`noGroup`](const-nogroup.md)
- [`separate`](const-separate.md)
- [`login`](const-login.md)
- [`admin`](const-admin.md)
- [`superuser`](const-superuser.md)
- [`allowMarkdown`](const-allowmarkdown.md)
- [`markdown`](const-markdown.md)
- [`allowDuplicate`](const-allowduplicate.md)
- [`duplicate`](const-duplicate.md)
