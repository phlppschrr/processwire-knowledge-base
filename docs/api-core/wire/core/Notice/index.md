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
- [`prepend = 1`](const-prepend.md)
- [`debug = 2`](const-debug.md)
- [`log = 8`](const-log.md)
- [`logOnly = 16`](const-logonly.md)
- [`allowMarkup = 32`](const-allowmarkup.md)
- [`markup = 32`](const-markup.md)
- [`anonymous = 65536`](const-anonymous.md)
- [`noGroup = 131072`](const-nogroup.md)
- [`separate = 131072`](const-separate.md)
- [`login = 262144`](const-login.md)
- [`admin = 524288`](const-admin.md)
- [`superuser = 1048576`](const-superuser.md)
- [`allowMarkdown = 4194304`](const-allowmarkdown.md)
- [`markdown = 4194304`](const-markdown.md)
- [`allowDuplicate = 8388608`](const-allowduplicate.md)
- [`duplicate = 8388608`](const-duplicate.md)
