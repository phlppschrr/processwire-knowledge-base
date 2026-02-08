# $wireShutdown->setFatalErrorResponse(array $options)

Source: `wire/core/WireShutdown.php`

Set fatal error response info including http code, optional extra headers, and more

## Arguments

- array $options - `code` (int): http code to send, or omit to use default (500) - `headers` (array): Optional additional headers to send, in format [ "Header-Name: Header-Value" ] - `emailTo` (string): Administrator email address to send error to (default=$config->adminEmail) - `emailFrom` (string): From email address for email to administrator (default=$config->wireMail['from']) - `emailFromName` (string): From “name” for email to administrator (default=$config->wireMail['fromName']) - `emailSubject` (string): Override email subject (default=use built-in translatable subject) - `emailBody` (string): Override default email body (text-only). Should have {url}, {user} and {message} placeholders. - `emailModule` (string): Name of WireMail module to use or leave blank for automatic. - `words` (array): Spicy but calming words to prepend to visible error messages.

## Meta

- @since 3.0.166
