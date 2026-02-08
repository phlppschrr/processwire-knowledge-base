# WireMail: other

Source: `wire/core/WireMail.php`

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
