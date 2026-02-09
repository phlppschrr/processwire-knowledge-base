# WireMail

Source: `wire/core/WireMail.php`

Inherits: `WireData`
Implements: `WireMailInterface`

## Summary

ProcessWire WireMail

Common methods:
- [`get()`](method-get.md)
- [`set()`](method-set.md)
- [`sanitizeEmail()`](method-sanitizeemail.md)
- [`sanitizeHeaderName()`](method-___sanitizeheadername.md)
- [`sanitizeHeaderValue()`](method-___sanitizeheadervalue.md)

Groups:
Group: [other](group-other.md)

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

## Methods
- [`__construct()`](method-__construct.md) Construct
- [`get(string $key): mixed|null`](method-get.md) Get property
- [`set(string $key, mixed $value): $this|WireData`](method-set.md) Set property
- [`sanitizeEmail(string $email): string`](method-sanitizeemail.md) Sanitize an email address or throw WireException if invalid or in blacklist
- [`sanitizeHeaderName(string $name): string`](method-___sanitizeheadername.md) (hookable) Sanitize and normalize a header name
- [`sanitizeHeaderValue(string $value): string`](method-___sanitizeheadervalue.md) (hookable) Sanitize an email header header value
- [`extractEmailAndName(string $email): array()`](method-extractemailandname.md) Given an email string like "User <user@example.com>" extract and return email and username separately
- [`bundleEmailAndName(string $email, string $name): string`](method-bundleemailandname.md) Given an email and name, bundle it to an RFC 2822 string
- [`to(string|array|null $email = null, string $name = null): $this`](method-to.md) Set the email to address
- [`toName(string $name): $this`](method-toname.md) Set the 'to' name
- [`from(string $email, $name = null): $this`](method-from.md) Set the email 'from' address and optionally name
- [`fromName(string $name): $this`](method-fromname.md) Set the 'from' name
- [`replyTo(string $email, $name = null): $this`](method-replyto.md) Set the 'reply-to' email address and optionally name (where supported)
- [`replyToName(string $name): $this`](method-replytoname.md) Set the 'reply-to' name (where supported)
- [`subject(string $subject): $this`](method-subject.md) Set the email subject
- [`body(string $body): $this`](method-body.md) Set the email message body (text only)
- [`bodyHTML(string $body): $this`](method-bodyhtml.md) Set the email message body (HTML only)
- [`header(string|array $key, string $value): $this`](method-header.md) Set any email header
- [`headers(array $headers): $this`](method-headers.md) Set multiple email headers using associative array
- [`param(string $value): $this`](method-param.md) Set any email param
- [`attachment(string $value, string $filename = ''): $this`](method-attachment.md) Add a file to be attached to the email
- [`multipartBoundary(string|bool $prefix = ''): string`](method-multipartboundary.md) Get the multipart boundary string for this email
- [`send(): int`](method-___send.md) (hookable) Send the email
- [`renderMailHeader(): string`](method-rendermailheader.md) Render email header string
- [`renderMailBody(): string`](method-rendermailbody.md) Render mail body
- [`renderMailAttachments(): string`](method-rendermailattachments.md) Render mail attachments string for placement in body
- [`strReplace(string $str, string|array $find, string $replace = ''): string`](method-strreplace.md) Recursive string replacement
- [`htmlToText(string $html): string`](method-___htmltotext.md) (hookable) Convert HTML mail body to TEXT mail body
- [`encodeSubject(string $subject): string`](method-encodesubject.md) Encode a subject, use mbstring if available
- [`findBestEncodePart(string $input, int $maxlen = 63, bool $isFirst = false): string`](method-findbestencodepart.md) Tries to split the passed subject at a whitespace at or before $maxlen, falling back to a hard substr if none was found, and returns the left part.
- [`quotedPrintableString(string $text): string`](method-quotedprintablestring.md) Return the text quoted-printable encoded
