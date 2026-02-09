# WireShutdown

Source: `wire/core/WireShutdown.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire shutdown handler


Look for errors at shutdown and log them, plus echo the error if the page is editable

Methods:
- [`__construct(Config $config)`](method-__construct.md) Construct and register shutdown function
- [`setFatalErrorResponse(array $options)`](method-setfatalerrorresponse.md) Set fatal error response info including http code, optional extra headers, and more
- [`prepareLabels()`](method-preparelabels.md) Setup our translation labels
- [`getErrorMessage(array $error): string`](method-geterrormessage.md) Create more informative error message from $error array
- [`getWireInput(): WireInput`](method-getwireinput.md) Get WireInput instance and create it if not already present in the API
- [`getCurrentUrl(): string`](method-getcurrenturl.md) Get the current request URL or "/?/" if it cannot be determined
- [`amendErrorMessage(string $message): string`](method-amenderrormessage.md) Add helpful info or replace error message with something better, when possible
- [`sendErrorMessage(string $message, string $why, bool $useHTML)`](method-senderrormessage.md) Render an error message and reason why
- [`simplifyErrorMessageHTML(string $html): string`](method-simplifyerrormessagehtml.md) Simplify error message HTML for output (inclusive of simplifyErrorMessageText also)
- [`simplifyErrorMessageText(string $text): string`](method-simplifyerrormessagetext.md) Simplify error message to remove unnecessary or redundant information
- [`seasonErrorMessage(string $message): string`](method-seasonerrormessage.md) Provide additional seasoning for error message during debug mode output
- [`sendFatalHeader(): int`](method-sendfatalheader.md) Send fatal error http header and return error code sent
- [`sendFatalError(string $message, bool $useHTML)`](method-sendfatalerror.md) Send a fatal error
- [`sendExistingOutput(): bool`](method-sendexistingoutput.md) Send any existing output while removing PHP’s error message from it (to avoid duplication)
- [`fatalError(array $error)`](method-___fatalerror.md) (hookable) Hook called when fatal error received by shutdown()
- [`setFatalError(\Throwable $e, string $message = '')`](method-setfatalerror.md) Set shutdown fatal error
- [`getError(): array`](method-geterror.md) Get last error
- [`shutdown(): bool`](method-shutdown.md) Shutdown function registered with PHP
- [`getReasonsWhy(): array`](method-getreasonswhy.md) Get reasons why a fatal error message is shown
- [`saveFatalLog(string $url, string $userName, string $message): bool`](method-savefatallog.md) Save fatal error to log
- [`sendFatalEmail(string $url, string $userName, string $message): bool`](method-sendfatalemail.md) Send fatal error email
- [`shutdownExternal()`](method-shutdownexternal.md) Secondary shutdown call when ProcessWire booted externally

Constants:
- [`defaultFatalErrorHTML`](const-defaultfatalerrorhtml.md)
- [`defaultEmailBody`](const-defaultemailbody.md)
