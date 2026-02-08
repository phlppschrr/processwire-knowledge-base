# Notification: other

Source: `wire/modules/System/SystemNotifications/Notification.php`

@property int $pages_id  page ID notification is for (likely a User page)

@property int $sort  sort value, as required by Fieldtype

@property int $src_id  page ID when notification was generated

@property string $title  title/headline

@property int $flags  flags: see flag constants

@property int $created  datetime created (unix timestamp)

@property int $modified  datetime created (unix timestamp)

@property int $qty  quantity of times this notification has been repeated

@property array $flagNames Notification flag names
