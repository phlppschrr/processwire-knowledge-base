# HTMLPurifier_Lexer_DirectLex

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Our in-house implementation of a parser.

A pure PHP parser, DirectLex has absolutely no dependencies, making
it a reasonably good default for PHP4.  Written with efficiency in mind,
it can be four times faster than HTMLPurifier_Lexer_PEARSax3, although it
pales in comparison to HTMLPurifier_Lexer_DOMLex.

@todo Reread XML spec and document differences.

## tokenizeHTML()

@param String $html
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return array|HTMLPurifier_Token[]

## substrCount()

PHP 5.0.x compatible substr_count that implements offset and length
@param string $haystack
@param string $needle
@param int $offset
@param int $length
@return int

## parseAttributeString()

Takes the inside of an HTML tag and makes an assoc array of attributes.

@param string $string Inside of tag excluding name.
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return array Assoc array of attributes.
