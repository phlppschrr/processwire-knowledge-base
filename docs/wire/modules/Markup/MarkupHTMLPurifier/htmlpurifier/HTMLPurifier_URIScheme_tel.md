# HTMLPurifier_URIScheme_tel

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates tel (for phone numbers).

The relevant specifications for this protocol are RFC 3966 and RFC 5341,
but this class takes a much simpler approach: we normalize phone
numbers so that they only include (possibly) a leading plus,
and then any number of digits and x'es.
