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

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [get()](method-get.md)
Method: [set()](method-set.md)
Method: [sanitizeEmail()](method-sanitizeemail.md)
Method: [sanitizeHeaderName()](method-___sanitizeheadername.md) (hookable)
Method: [sanitizeHeaderValue()](method-___sanitizeheadervalue.md) (hookable)
Method: [extractEmailAndName()](method-extractemailandname.md)
Method: [bundleEmailAndName()](method-bundleemailandname.md)
Method: [to()](method-to.md)
Method: [toName()](method-toname.md)
Method: [from()](method-from.md)
Method: [fromName()](method-fromname.md)
Method: [replyTo()](method-replyto.md)
Method: [replyToName()](method-replytoname.md)
Method: [subject()](method-subject.md)
Method: [body()](method-body.md)
Method: [bodyHTML()](method-bodyhtml.md)
Method: [header()](method-header.md)
Method: [headers()](method-headers.md)
Method: [param()](method-param.md)
Method: [attachment()](method-attachment.md)
Method: [multipartBoundary()](method-multipartboundary.md)
Method: [send()](method-___send.md) (hookable)
Method: [renderMailHeader()](method-rendermailheader.md)
Method: [renderMailBody()](method-rendermailbody.md)
Method: [renderMailAttachments()](method-rendermailattachments.md)
Method: [strReplace()](method-strreplace.md)
Method: [htmlToText()](method-___htmltotext.md) (hookable)
Method: [encodeSubject()](method-encodesubject.md)
Method: [findBestEncodePart()](method-findbestencodepart.md)
Method: [quotedPrintableString()](method-quotedprintablestring.md)
