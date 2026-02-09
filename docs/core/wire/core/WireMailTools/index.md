# WireMailTools

Source: `wire/core/WireMailTools.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire Mail Tools ($mail API variable)


Provides an API interface to email and WireMail.
~~~~~
// Simple usage example
$message = $mail->new();
$message->subject('Hello world')
  ->to('user@domain.com')
  ->from('you@company.com')
  ->body('Hello there big world')
  ->bodyHTML('<h2>Hello there big world</h2>');
$numSent = $message->send();

// ProcessWire 3.0.113 lets you skip the $mail->new() call if you want:
$numSent = $mail->subject('Hello world')
  ->to('user@domain.com')
  ->from('you@company.com')
  ->body('Hello there big world')
  ->bodyHTML('<h2>Hello there big world</h2>')
  ->send();
~~~~~

Methods:
- [`new(array|string $options = array()): WireMail`](method-___new.md) (hookable)
- [`send(string|array $to = '', string $from = '', string $subject = '', string|array $body = '', array|string $options = array()): int|WireMail`](method-send.md)
- [`sendHTML(string|array $to = '', string $from = '', string $subject = '', string $bodyHTML = '', array|string $options = array()): int|WireMail`](method-sendhtml.md)
- [`mail(string|array $to, string $subject, string|array $message, array $headers = array()): bool`](method-mail.md)
- [`mailHTML(string|array $to, string $subject, $messageHTML, array $headers = array()): bool`](method-mailhtml.md)
- [`to(string|array $email, string $name = null): WireMail`](method-to.md)
- [`from(string $email, $name = null): WireMail`](method-from.md)
- [`subject(string $subject): WireMail`](method-subject.md)
- [`isBlacklistEmail(string $email, array $options = array()): bool|string`](method-___isblacklistemail.md) (hookable)
