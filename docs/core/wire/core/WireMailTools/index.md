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
Method: [new()](method-___new.md) (hookable)
Method: [send()](method-send.md)
Method: [sendHTML()](method-sendhtml.md)
Method: [mail()](method-mail.md)
Method: [mailHTML()](method-mailhtml.md)
Method: [to()](method-to.md)
Method: [from()](method-from.md)
Method: [subject()](method-subject.md)
Method: [isBlacklistEmail()](method-___isblacklistemail.md) (hookable)
