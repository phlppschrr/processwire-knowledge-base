# Notification

Source: `wire/modules/System/SystemNotifications/Notification.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

An individual notification item to be part of a NotificationArray for a Page

@class Notification


data encoded vars, all optional
===============================

- `$id: int` unique ID (among others the user may have)
- `$text: string` extended text
- `$html: string` extended text as HTML markup
- `$from: string` "from" text where applicable, like a class name
- `$icon: string` fa-icon when applicable
- `$href: string` clicking notification goes to this URL
- `$progress: int` progress percent 0-100
- `$expires: int` datetime after which will automatically be deleted

Methods:
- [`__construct()`](method-__construct.md)
- [`is(string $name): bool`](method-is.md)
- [`flagNameToFlag(string $name): int`](method-flagnametoflag.md)
- [`flagNamesToFlags(string $names): array`](method-flagnamestoflags.md)
- [`setFlag(string|int $name, bool $add = true): self`](method-setflag.md)
- [`addFlag(string $name): self`](method-addflag.md)
- [`removeFlag(string $name): self`](method-removeflag.md)
- [`setFlags(string $names, bool $add = true): self`](method-setflags.md)
- [`set(string $key, mixed $value): self|Notification|WireData`](method-set.md)
- [`getID(): mixed|null|string`](method-getid.md)
- [`getHash(): string`](method-gethash.md)
- [`get(string $key): mixed`](method-get.md)
- [`isExpired(): bool`](method-isexpired.md)
- [`__toString(): string`](method-__tostring.md)

Constants:
- [`flagDebug`](const-flagdebug.md)
