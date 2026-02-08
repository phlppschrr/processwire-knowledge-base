# HTMLPurifier_Language

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Represents a language and defines localizable string formatting and
other functions, as well as the localized messages for HTML Purifier.

## load()

Loads language object with necessary info from factory cache
@note This is a lazy loader

## getMessage()

Retrieves a localised message.
@param string $key string identifier of message
@return string localised message

## getErrorName()

Retrieves a localised error name.
@param int $int error number, corresponding to PHP's error reporting
@return string localised message

## listify()

Converts an array list into a string readable representation
@param array $array
@return string

## formatMessage()

Formats a localised message with passed parameters
@param string $key string identifier of message
@param array $args Parameters to substitute in
@return string localised message
@todo Implement conditionals? Right now, some messages make
    reference to line numbers, but those aren't always available
