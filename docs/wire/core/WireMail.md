# WireMail

Source: `wire/core/WireMail.php`

ProcessWire WireMail

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

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

## other

@method int send() Send email.

@method string htmlToText($html) Convert HTML email body to TEXT email body.

@property array $to To email address.

@property array $toName Optional person’s name to accompany “to” email address

@property string $from From email address.

@property string $fromName Optional person’s name to accompany “from” email address.

@property string $replyTo Reply-to email address (where supported).

@property string $replyToName Optional person’s name to accompany “reply-to” email address.

@property string $subject Subject line of email.

@property string $body Plain text body of email.

@property string $bodyHTML HTML body of email.

@property array $header Associative array of additional headers.

@property array $headers Alias of $header

@property array $param Associative array of aditional params (likely not applicable to most WireMail modules).

@property array $attachments Array of file attachments (if populated and where supported)

@property string $newline Newline character, populated only if different from CRLF.

## __construct()

Construct

## get()

Get property

@param string $key

@return mixed|null

## set()

Set property

@param string $key

@param mixed $value

@return $this|WireData

## sanitizeEmail()

Sanitize an email address or throw WireException if invalid or in blacklist

@param string $email

@return string

@throws WireException

## ___sanitizeHeaderName()

Sanitize and normalize a header name

@param string $name

@return string

@since 3.0.132

## ___sanitizeHeaderValue()

Sanitize an email header header value

@param string $value

@return string

@since 3.0.132

## extractEmailAndName()

Given an email string like "User <user@example.com>" extract and return email and username separately

@param string $email

@return array() Index 0 contains email, index 1 contains username or blank if not set

## bundleEmailAndName()

Given an email and name, bundle it to an RFC 2822 string

If name is blank, then just the email will be returned

@param string $email

@param string $name

@return string

## to()

Set the email to address

Each added email addresses appends to any addresses already supplied, unless
you specify NULL as the email address, in which case it clears them all.

@param string|array|null $email Specify any ONE of the following:
- Single email address or "User Name <user@example.com>" string.
- CSV string of #1.
- Non-associative array of #1.
- Associative array of (email => name)
- NULL (default value, to clear out any previously set values)

@param string $name Optionally provide a TO name, applicable
	only when specifying #1 (single email) for the first argument.

@return $this

@throws WireException if any provided emails were invalid or in blacklist

## toName()

Set the 'to' name

It is preferable to do this with the to() method, but this is provided to ensure that
all properties can be set with direct access, i.e. $mailer->toName = 'User Name';

This sets the 'to name' for whatever the last added 'to' email address was.

@param string $name The 'to' name

@return $this

@throws WireException if you attempt to set a toName before a to email.

## from()

Set the email 'from' address and optionally name

@param string $email Must be a single email address or "User Name <user@example.com>" string.

@param string|null An optional FROM name (same as setting/calling fromName)

@return $this

@throws WireException if provided email was invalid or in blacklist

## fromName()

Set the 'from' name

It is preferable to do this with the from() method, but this is provided to ensure that
all properties can be set with direct access, i.e. $mailer->fromName = 'User Name';

@param string $name The 'from' name

@return $this

## replyTo()

Set the 'reply-to' email address and optionally name (where supported)

@param string $email Must be a single email address or "User Name <user@example.com>" string.

@param string|null An optional Reply-To name (same as setting/calling replyToName method)

@return $this

@throws WireException if provided email was invalid or in blacklist

## replyToName()

Set the 'reply-to' name (where supported)

@param string $name

@return $this

## subject()

Set the email subject

@param string $subject Email subject text

@return $this

## body()

Set the email message body (text only)

~~~~~
$m = wireMail();
$m->body('Hello world');
~~~~~

@param string $body Email body in text only

@return $this

## bodyHTML()

Set the email message body (HTML only)

This should be the text from an entire HTML document, not just an element.

~~~~~
$m = wireMail();
$m->bodyHTML('<html><body><h1>Hello world</h1></body></html>');
~~~~~

@param string $body Email body in HTML

@return $this

## header()

Set any email header

- Multiple calls will append existing headers.
- To remove an existing header, specify NULL as the value.


@param string|array $key Header name

@param string $value Header value or specify null to unset

@return $this

## headers()

Set multiple email headers using associative array

@param array $headers

@return $this

## param()

Set any email param

See `$additional_parameters` at <http://www.php.net/manual/en/function.mail.php>

- Multiple calls will append existing params.
- To remove an existing param, specify NULL as the value.

This function may only be applicable if you don't have other WireMail modules
installed as email params are only used by PHP's `mail()` function.


@param string $value

@return $this

## attachment()

Add a file to be attached to the email

~~~~~~
$m = wireMail();
$m->to('user@domain.com')->from('hello@world.com');
$m->subject('Test attachment');
$m->body('This is just a test of a file attachment');
$m->attachment('/path/to/file.jpg');
$m->send();
~~~~~~


- Multiple calls will append attachments.
- To remove the supplied attachments, specify NULL as the value.
- Attachments may or may not be supported by 3rd party WireMail modules.

@param string $value Full path and filename of file attachment

@param string $filename Optional different basename for file as it appears in the mail

@return $this

## multipartBoundary()

Get the multipart boundary string for this email

@param string|bool $prefix Specify optional boundary prefix or boolean true to clear any existing stored boundary

@return string

## ___send()

Send the email

Call this method only after you have specified at least the `subject`, `to` and `body`.


@return int Returns a positive number (indicating number of addresses emailed) or 0 on failure.

## renderMailHeader()

Render email header string

@return string

## renderMailBody()

Render mail body

@return string

## renderMailAttachments()

Render mail attachments string for placement in body

@return string

## strReplace()

Recursive string replacement

This is better than using str_replace() because it handles cases where replacement
results in the construction of a new $find that was not present in original $str.
Note: this function ignores case.

@param string $str

@param string|array $find

@param string $replace

@return string

## ___htmlToText()

Convert HTML mail body to TEXT mail body

@param string $html

@return string

## encodeSubject()

Encode a subject, use mbstring if available


@param string $subject

@return string

## findBestEncodePart()

Tries to split the passed subject at a whitespace at or before $maxlen,
falling back to a hard substr if none was found, and returns the
left part.

Makes sure that the quoted-printable encoded part is inside the 76 characters
header limit (66 for first line that has the header name, minus a buffer
of 2 characters for whitespace) given in rfc2047.

@param string $input The subject to encode

@param int $maxlen Maximum length of unencoded string, defaults to 63

@param bool $isFirst Set to true for first line to account for the header name

@return string

## quotedPrintableString()

Return the text quoted-printable encoded

Uses short notation for charset and encoding suitable for email headers
as laid out in rfc2047.


@param string $text

@return string
