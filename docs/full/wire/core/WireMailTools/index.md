# WireMailTools

Source: `wire/core/WireMailTools.php`

ProcessWire Mail Tools ($mail API variable)

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

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

Groups:
Group: [other](group-other.md)

Methods:
Method: [___new()](method-___new.md)
Method: [send()](method-send.md)
Method: [sendHTML()](method-sendhtml.md)
Method: [mail()](method-mail.md)
Method: [mailHTML()](method-mailhtml.md)
Method: [to()](method-to.md)
Method: [from()](method-from.md)
Method: [subject()](method-subject.md)
Method: [___isBlacklistEmail()](method-___isblacklistemail.md)
