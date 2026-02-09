# Notification: other

Source: `wire/modules/System/SystemNotifications/Notification.php`

- $pages_id: int page ID notification is for (likely a User page)

- $sort: int sort value, as required by Fieldtype

- $src_id: int page ID when notification was generated

- $title: string title/headline

- $flags: int flags: see flag constants

- $created: int datetime created (unix timestamp)

- $modified: int datetime created (unix timestamp)

- $qty: int quantity of times this notification has been repeated

- $flagNames: array Notification flag names
