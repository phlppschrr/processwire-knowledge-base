# HTMLPurifier_AttrCollections

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Defines common attribute collections that modules reference

## performInclusions()

Takes a reference to an attribute associative array and performs
all inclusions specified by the zero index.
@param array &$attr Reference to attribute array

## expandIdentifiers()

Expands all string identifiers in an attribute array by replacing
them with the appropriate values inside HTMLPurifier_AttrTypes
@param array &$attr Reference to attribute array
@param HTMLPurifier_AttrTypes $attr_types HTMLPurifier_AttrTypes instance
