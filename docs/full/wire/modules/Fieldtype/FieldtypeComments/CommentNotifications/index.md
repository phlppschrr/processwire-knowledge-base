# CommentNotifications

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

Methods:
- [`setMailer(string $mailer)`](method-setmailer.md)
- [`newMail(): WireMail`](method-newmail.md)
- [`sendAdminNotificationEmail(Comment $comment): int`](method-___sendadminnotificationemail.md) (hookable)
- [`parseEmails($str): array`](method-parseemails.md)
- [`checkActions(): array(`](method-checkactions.md)
- [`modifyNotifications(string $subcode, bool $enable, bool $all = false): bool`](method-modifynotifications.md)
- [`sendNotificationEmail(Comment $comment, string|array $email, string $subcode, array $options = array()): int`](method-___sendnotificationemail.md) (hookable)
- [`sendConfirmationEmail(Comment $comment, $email, $subcode): mixed`](method-___sendconfirmationemail.md) (hookable)
