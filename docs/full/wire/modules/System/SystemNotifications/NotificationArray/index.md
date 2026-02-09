# NotificationArray

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Inherits: `WireArray`

Contains multiple Event objects for a single page

@class NotificationArray

Methods:
- [`__construct(Page $page)`](method-__construct.md) Create a new NotificationArray
- [`isValidItem(Notification $item): bool`](method-isvaliditem.md) Template method from WireArray
- [`add(Notification $item): self|NotificationArray|WireArray`](method-add.md) Add a Notification instance to this NotificationArray
- [`get(int|string $key): Notification|null`](method-get.md) Retrieve a Notification by index or by id
- [`getBy(string $property, mixed $value): null|Notification`](method-getby.md) Get a notification that contains the given value for $property
- [`save(): bool`](method-save.md) Save any changes or additions that were made to these Notifications
- [`__toString(): string`](method-__tostring.md) Get string value of this NotificationArray
- [`getNew(string $flag = 'message', bool $addNow = true): Notification`](method-getnew.md) Get a new Notification
- [`message($text, $flags = 0)`](method-message.md) *********************************************************************************** The following methods are based on those in the base Wire class, but they override them to replace Notices functionality with Notifications
- [`message(string $text, int|bool $flags = 0): Notification`](method-message.md) Record an informational or 'success' message
- [`warning(string $text, int|bool $flags = 0): Notification`](method-warning.md) Record a warning notification
- [`error(string $text, int|bool $flags = 0): Notification`](method-error.md) Record an error notification
- [`errors(string|array $options = array()): Notices|string`](method-errors.md) Return all error Notifications
- [`warnings(string|array $options = array()): Notices|string`](method-warnings.md) Return warnings recorded by this object
- [`messages(string|array $options = array()): Notices|string`](method-messages.md) Return messages recorded by this object
