# Notification

Source: `wire/modules/System/SystemNotifications/Notification.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

An individual notification item to be part of a NotificationArray for a Page

@class Notification


## Data Encoded Vars, All Optional

- `$id: int` unique ID (among others the user may have)
- `$text: string` extended text
- `$html: string` extended text as HTML markup
- `$from: string` "from" text where applicable, like a class name
- `$icon: string` fa-icon when applicable
- `$href: string` clicking notification goes to this URL
- `$progress: int` progress percent 0-100
- `$expires: int` datetime after which will automatically be deleted

Methods:
- [`__construct()`](method-__construct.md) Construct a new Notification
- [`is(string $name): bool`](method-is.md) Does this Notification match the given flag name(s)?
- [`flagNameToFlag(string $name): int`](method-flagnametoflag.md) Given a flag name, return the corresponding flag value
- [`flagNamesToFlags(string $names): array`](method-flagnamestoflags.md) Given multiple space separated flag names, return array of flag values
- [`setFlag(string|int $name, bool $add = true): self`](method-setflag.md) Set a named flag
- [`addFlag(string $name): self`](method-addflag.md) Add the given flag name(s) (shortcut for setFlag)
- [`removeFlag(string $name): self`](method-removeflag.md) Remove the given flag name(s) (shortcut for setFlag)
- [`setFlags(string $names, bool $add = true): self`](method-setflags.md) Set multiple flags
- [`set(string $key, mixed $value): self|Notification|WireData`](method-set.md) Set a value to the Notification
- [`getID(): mixed|null|string`](method-getid.md) Return an ID string/hash unique to this Notification within the page that its on
- [`getHash(): string`](method-gethash.md) Return an string hash for comparing other notifications to see if they contain the same content
- [`get(string $key): mixed`](method-get.md) Retrieve a value from the Notification
- [`isExpired(): bool`](method-isexpired.md) Is this Notification expired?
- [`__toString(): string`](method-__tostring.md) String value of a Notification

Constants:
- [`flagDebug`](const-flagdebug.md)
