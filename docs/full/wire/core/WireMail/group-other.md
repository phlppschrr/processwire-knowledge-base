# WireMail: other

Source: `wire/core/WireMail.php`

- [send(): int](method-___send.md) Send email.

- [htmlToText($html): string](method-___htmltotext.md) Convert HTML email body to TEXT email body.

- [$to: array](method-to.md) To email address.

- [$toName: array](method-toname.md) Optional person’s name to accompany “to” email address

- [$from: string](method-from.md) From email address.

- [$fromName: string](method-fromname.md) Optional person’s name to accompany “from” email address.

- [$replyTo: string](method-replyto.md) Reply-to email address (where supported).

- [$replyToName: string](method-replytoname.md) Optional person’s name to accompany “reply-to” email address.

- [$subject: string](method-subject.md) Subject line of email.

- [$body: string](method-body.md) Plain text body of email.

- [$bodyHTML: string](method-bodyhtml.md) HTML body of email.

- [$header: array](method-header.md) Associative array of additional headers.

- [$headers: array](method-headers.md) Alias of $header

- [$param: array](method-param.md) Associative array of aditional params (likely not applicable to most WireMail modules).

- $attachments: array Array of file attachments (if populated and where supported)

- $newline: string Newline character, populated only if different from CRLF.
