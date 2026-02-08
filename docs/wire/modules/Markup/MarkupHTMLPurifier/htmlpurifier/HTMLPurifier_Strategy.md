# HTMLPurifier_Strategy

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Supertype for classes that define a strategy for modifying/purifying tokens.

While HTMLPurifier's core purpose is fixing HTML into something proper,
strategies provide plug points for extra configuration or even extra
features, such as custom tags, custom parsing of text, etc.
