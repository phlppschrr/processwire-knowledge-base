# WireMailInterface

Source: `wire/core/WireMailInterface.php`

ProcessWire WireMail Interface

Methods:
- [`to(string|array|null $email = null, string $name = null): self`](method-to.md) Set the email to address
- [`from($email, $name = null): self`](method-from.md) Set the email from address
- [`subject(string $subject): self`](method-subject.md) Set the email subject
- [`body(string $body): self`](method-body.md) Set the email message body (text only)
- [`bodyHTML(string $body): self`](method-bodyhtml.md) Set the email message body (HTML only)
- [`header(string $key, string $value): self`](method-header.md) Set any email header
- [`param(string $value): self`](method-param.md) Set any email param
- [`send(): self`](method-___send.md) (hookable) Add a file to be attached to the email
- [`send(): int`](method-___send.md) (hookable) Send the email
