# WireShutdown

Source: `wire/core/WireShutdown.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire shutdown handler


Look for errors at shutdown and log them, plus echo the error if the page is editable

Methods:
- [`__construct(Config $config)`](method-__construct.md)
- [`setFatalErrorResponse(array $options)`](method-setfatalerrorresponse.md)
- [`prepareLabels()`](method-preparelabels.md)
- [`getErrorMessage(array $error): string`](method-geterrormessage.md)
- [`getWireInput(): WireInput`](method-getwireinput.md)
- [`getCurrentUrl(): string`](method-getcurrenturl.md)
- [`amendErrorMessage(string $message): string`](method-amenderrormessage.md)
- [`sendErrorMessage(string $message, string $why, bool $useHTML)`](method-senderrormessage.md)
- [`simplifyErrorMessageHTML(string $html): string`](method-simplifyerrormessagehtml.md)
- [`simplifyErrorMessageText(string $text): string`](method-simplifyerrormessagetext.md)
- [`seasonErrorMessage(string $message): string`](method-seasonerrormessage.md)
- [`sendFatalHeader(): int`](method-sendfatalheader.md)
- [`sendFatalError(string $message, bool $useHTML)`](method-sendfatalerror.md)
- [`sendExistingOutput(): bool`](method-sendexistingoutput.md)
- [`fatalError(array $error)`](method-___fatalerror.md) (hookable)
- [`setFatalError(\Throwable $e, string $message = '')`](method-setfatalerror.md)
- [`getError(): array`](method-geterror.md)
- [`shutdown(): bool`](method-shutdown.md)
- [`getReasonsWhy(): array`](method-getreasonswhy.md)
- [`saveFatalLog(string $url, string $userName, string $message): bool`](method-savefatallog.md)
- [`sendFatalEmail(string $url, string $userName, string $message): bool`](method-sendfatalemail.md)
- [`shutdownExternal()`](method-shutdownexternal.md)

Constants:
- [`defaultFatalErrorHTML`](const-defaultfatalerrorhtml.md)
- [`defaultEmailBody`](const-defaultemailbody.md)
