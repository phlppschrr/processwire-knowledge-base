# CommentNotifications

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

Methods:
- [`setMailer(string $mailer)`](method-setmailer.md) Set name of WireMail module to use for sending notifications
- [`newMail(): WireMail`](method-newmail.md)
- [`sendAdminNotificationEmail(Comment $comment): int`](method-___sendadminnotificationemail.md) (hookable) Send notification email to specified admin to review the comment
- [`parseEmails($str): array`](method-parseemails.md) Given a string containing emails or references to them, convert to array of emails
- [`checkActions(): array(`](method-checkactions.md) Check for a GET variable comment approval code and take action is valid
- [`modifyNotifications(string $subcode, bool $enable, bool $all = false): bool`](method-modifynotifications.md) Given a subscriber code, modify notifications on any comments where their email is present
- [`sendNotificationEmail(Comment $comment, string|array $email, string $subcode, array $options = array()): int`](method-___sendnotificationemail.md) (hookable) Send a user (not admin) notification email
- [`sendConfirmationEmail(Comment $comment, $email, $subcode): mixed`](method-___sendconfirmationemail.md) (hookable) Send confirmation/opt-in email for notifications (not yet active)
