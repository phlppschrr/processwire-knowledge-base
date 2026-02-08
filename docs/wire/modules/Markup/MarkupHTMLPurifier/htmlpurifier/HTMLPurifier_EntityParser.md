# HTMLPurifier_EntityParser

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Handles referencing and derefencing character entities

## substituteAttrEntities()

Substitute entities with the parsed equivalents.  Use this on
attribute contents in documents.

@param string $string String to have entities parsed.
@return string Parsed string.

## entityCallback()

Callback function for substituteNonSpecialEntities() that does the work.

@param array $matches  PCRE matches array, with 0 the entire match, and
                 either index 1, 2 or 3 set with a hex value, dec value,
                 or string (respectively).
@return string Replacement string.

## substituteNonSpecialEntities()

Callback regex string for parsing entities.
@type string
/
protected $_substituteEntitiesRegex =
'/&(?:[#]x([a-fA-F0-9]+)|[#]0*(\d+)|([A-Za-z_:][A-Za-z0-9.\-_:]*));?/';
//     1. hex             2. dec      3. string (XML style)

/**
Decimal to parsed string conversion table for special entities.
@type array
/
protected $_special_dec2str =
array(
34 => '"',
38 => '&',
39 => "'",
60 => '<',
62 => '>'
);

/**
Stripped entity names to decimal conversion table for special entities.
@type array
/
protected $_special_ent2dec =
array(
'quot' => 34,
'amp'  => 38,
'lt'   => 60,
'gt'   => 62
);

/**
Substitutes non-special entities with their parsed equivalents. Since
running this whenever you have parsed character is t3h 5uck, we run
it before everything else.

@param string $string String to have non-special entities parsed.
@return string Parsed string.

## nonSpecialEntityCallback()

Callback function for substituteNonSpecialEntities() that does the work.

@param array $matches  PCRE matches array, with 0 the entire match, and
                 either index 1, 2 or 3 set with a hex value, dec value,
                 or string (respectively).
@return string Replacement string.

## substituteSpecialEntities()

Substitutes only special entities with their parsed equivalents.

@notice We try to avoid calling this function because otherwise, it
would have to be called a lot (for every parsed section).

@param string $string String to have non-special entities parsed.
@return string Parsed string.

## specialEntityCallback()

Callback function for substituteSpecialEntities() that does the work.

This callback has same syntax as nonSpecialEntityCallback().

@param array $matches  PCRE-style matches array, with 0 the entire match, and
                 either index 1, 2 or 3 set with a hex value, dec value,
                 or string (respectively).
@return string Replacement string.
