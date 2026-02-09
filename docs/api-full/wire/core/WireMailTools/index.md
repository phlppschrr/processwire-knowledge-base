# WireMailTools

Source: `wire/core/WireMailTools.php`

Inherits: `Wire`

## Summary

ProcessWire Mail Tools (`$mail` API variable)

Common methods:
- [`new()`](method-___new.md)
- [`send()`](method-send.md)
- [`sendHTML()`](method-sendhtml.md)
- [`mail()`](method-mail.md)
- [`mailHTML()`](method-mailhtml.md)

Groups:
Group: [other](group-other.md)

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

## Methods
- [`new(array|string $options = array()): WireMail`](method-___new.md) (hookable) Get a new WireMail instance for sending email
- [`send(string|array $to = '', string $from = '', string $subject = '', string|array $body = '', array|string $options = array()): int|WireMail`](method-send.md) Send an email
- [`sendHTML(string|array $to = '', string $from = '', string $subject = '', string $bodyHTML = '', array|string $options = array()): int|WireMail`](method-sendhtml.md) Send an email with given message text assumed to be HTML
- [`mail(string|array $to, string $subject, string|array $message, array $headers = array()): bool`](method-mail.md) Send an email, drop-in replacement for PHP mail() that uses the same arguments
- [`mailHTML(string|array $to, string $subject, $messageHTML, array $headers = array()): bool`](method-mailhtml.md) Send an email with message assumed to be in HTML
- [`to(string|array $email, string $name = null): WireMail`](method-to.md) Return new WireMail instance populated with “to” email
- [`from(string $email, $name = null): WireMail`](method-from.md) Return new WireMail instance populated with “from” email
- [`subject(string $subject): WireMail`](method-subject.md) Return new WireMail instance populated with subject
- [`isBlacklistEmail(string $email, array $options = array()): bool|string`](method-___isblacklistemail.md) (hookable) Is given email address in the blacklist?
