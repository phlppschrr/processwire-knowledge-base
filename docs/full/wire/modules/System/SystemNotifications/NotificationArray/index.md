# NotificationArray

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Inherits: `WireArray`

Contains multiple Event objects for a single page

@class NotificationArray

Methods:
- [`__construct(Page $page)`](method-__construct.md)
- [`isValidItem(Notification $item): bool`](method-isvaliditem.md)
- [`add(Notification $item): self|NotificationArray|WireArray`](method-add.md)
- [`get(int|string $key): Notification|null`](method-get.md)
- [`getBy(string $property, mixed $value): null|Notification`](method-getby.md)
- [`save(): bool`](method-save.md)
- [`__toString(): string`](method-__tostring.md)
- [`getNew(string $flag = 'message', bool $addNow = true): Notification`](method-getnew.md)
- [`message($text, $flags = 0)`](method-message.md)
- [`message(string $text, int|bool $flags = 0): Notification`](method-message.md)
- [`warning(string $text, int|bool $flags = 0): Notification`](method-warning.md)
- [`error(string $text, int|bool $flags = 0): Notification`](method-error.md)
- [`errors(string|array $options = array()): Notices|string`](method-errors.md)
- [`warnings(string|array $options = array()): Notices|string`](method-warnings.md)
- [`messages(string|array $options = array()): Notices|string`](method-messages.md)
