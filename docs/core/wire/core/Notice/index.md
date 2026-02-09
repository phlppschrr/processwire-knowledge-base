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
- [`__construct(string $text, int|string|array $flags = 0)`](method-__construct.md)
- [`set(string $key, mixed $value): $this|WireData`](method-set.md)
- [`get(string $key): mixed`](method-get.md)
- [`flags(string|int|array|null $value = null): int`](method-flags.md)
- [`flag(string|int $name): int`](method-flag.md)
- [`flagNames(null|int $flags = null, bool $getString = false): array|string`](method-flagnames.md)
- [`addFlag(int|string $flag)`](method-addflag.md)
- [`removeFlag(int|string $flag)`](method-removeflag.md)
- [`hasFlag(int|string $flag): bool`](method-hasflag.md)
- [`getName(): string`](method-getname.md)
- [`viewable(): bool`](method-viewable.md)

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
