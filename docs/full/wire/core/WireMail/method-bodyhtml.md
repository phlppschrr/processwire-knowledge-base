# WireMail::bodyHTML()

Source: `wire/core/WireMail.php`

Set the email message body (HTML only)

This should be the text from an entire HTML document, not just an element.

~~~~~
$m = wireMail();
$m->bodyHTML('<html><body><h1>Hello world</h1></body></html>');
~~~~~

@param string $body Email body in HTML

@return $this
