# WireMail

Source: `wire/core/WireMail.php`

Inherits: `WireData`
Implements: `WireMailInterface`


Groups:
Group: [other](group-other.md)

ProcessWire WireMail


A module type that handles sending of email in ProcessWire
$m

Below are 2 different ways you can get a new instance of WireMail.
~~~~~
$m = $mail->new(); // option A: use $mail API variable
$m = wireMail(); // option B: use wireMail() function
~~~~~
Once you have an instance of WireMail (`$m`), you can use it to send email like in these examples below.
~~~~~
// chained (fluent) method call usage
$m->to('user@domain.com')
  ->from('you@company.com')
  ->subject('Message Subject')
  ->body('Optional message body in plain text')
  ->bodyHTML('<html><body><p>Optional message body in HTML</p></body></html>')
  ->send();

// separate method call usage
$m->to('user@domain.com'); // specify CSV string or array for multiple addresses
$m->from('you@company.com');
$m->subject('Message Subject');
$m->body('Message Body');
$m->send();

// optionally specify “from” or “to” names as 2nd argument
$m->to('user@domain.com', 'John Smith');
$m->from('you@company.com', 'Mary Jane');

// other methods or properties you might set (or get)
$m->fromName('Mary Jane');
$m->toName('John Smith');
$m->replyTo('somebody@somewhere.com');
$m->replyToName('Joe Somebody');
$m->attachment('/path/to/file.ext');
$m->header('X-Mailer', 'ProcessWire');
$m->param('-f you@company.com'); // PHP mail() param (envelope from example)

// note that the send() function always returns the quantity of messages sent
$numSent = $m->send();
~~~~~

Methods:
- [`__construct()`](method-__construct.md)
- [`get(string $key): mixed|null`](method-get.md)
- [`set(string $key, mixed $value): $this|WireData`](method-set.md)
- [`sanitizeEmail(string $email): string`](method-sanitizeemail.md)
- [`sanitizeHeaderName(string $name): string`](method-___sanitizeheadername.md) (hookable)
- [`sanitizeHeaderValue(string $value): string`](method-___sanitizeheadervalue.md) (hookable)
- [`extractEmailAndName(string $email): array()`](method-extractemailandname.md)
- [`bundleEmailAndName(string $email, string $name): string`](method-bundleemailandname.md)
- [`to(string|array|null $email = null, string $name = null): $this`](method-to.md)
- [`toName(string $name): $this`](method-toname.md)
- [`from(string $email, $name = null): $this`](method-from.md)
- [`fromName(string $name): $this`](method-fromname.md)
- [`replyTo(string $email, $name = null): $this`](method-replyto.md)
- [`replyToName(string $name): $this`](method-replytoname.md)
- [`subject(string $subject): $this`](method-subject.md)
- [`body(string $body): $this`](method-body.md)
- [`bodyHTML(string $body): $this`](method-bodyhtml.md)
- [`header(string|array $key, string $value): $this`](method-header.md)
- [`headers(array $headers): $this`](method-headers.md)
- [`param(string $value): $this`](method-param.md)
- [`attachment(string $value, string $filename = ''): $this`](method-attachment.md)
- [`multipartBoundary(string|bool $prefix = ''): string`](method-multipartboundary.md)
- [`send(): int`](method-___send.md) (hookable)
- [`renderMailHeader(): string`](method-rendermailheader.md)
- [`renderMailBody(): string`](method-rendermailbody.md)
- [`renderMailAttachments(): string`](method-rendermailattachments.md)
- [`strReplace(string $str, string|array $find, string $replace = ''): string`](method-strreplace.md)
- [`htmlToText(string $html): string`](method-___htmltotext.md) (hookable)
- [`encodeSubject(string $subject): string`](method-encodesubject.md)
- [`findBestEncodePart(string $input, int $maxlen = 63, bool $isFirst = false): string`](method-findbestencodepart.md)
- [`quotedPrintableString(string $text): string`](method-quotedprintablestring.md)
