# HTMLPurifier_Generator

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Generates HTML from tokens.
@todo Refactor interface so that configuration/context is determined
      upon instantiation, no need for messy generateFromTokens() calls
@todo Make some of the more internal functions protected, and have
      unit tests work around that

## generateFromTokens()

Generates HTML from an array of tokens.
@param HTMLPurifier_Token[] $tokens Array of HTMLPurifier_Token
@return string Generated HTML

## generateFromToken()

Generates HTML from a single token.
@param HTMLPurifier_Token $token HTMLPurifier_Token object.
@return string Generated HTML

## generateScriptFromToken()

Special case processor for the contents of script tags
@param HTMLPurifier_Token $token HTMLPurifier_Token object.
@return string
@warning This runs into problems if there's already a literal
         --> somewhere inside the script contents.

## generateAttributes()

Generates attribute declarations from attribute array.
@note This does not include the leading or trailing space.
@param array $assoc_array_of_attributes Attribute array
@param string $element Name of element attributes are for, used to check
       attribute minimization.
@return string Generated HTML fragment for insertion.

## escape()

Escapes raw text data.
@todo This really ought to be protected, but until we have a facility
      for properly generating HTML here w/o using tokens, it stays
      public.
@param string $string String data to escape for HTML.
@param int $quote Quoting style, like htmlspecialchars. ENT_NOQUOTES is
              permissible for non-attribute output.
@return string escaped data.
