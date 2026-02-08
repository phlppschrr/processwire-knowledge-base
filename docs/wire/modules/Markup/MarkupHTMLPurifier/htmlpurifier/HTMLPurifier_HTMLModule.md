# HTMLPurifier_HTMLModule

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Represents an XHTML 1.1 module, with information on elements, tags
and attributes.
@note Even though this is technically XHTML 1.1, it is also used for
      regular HTML parsing. We are using modulization as a convenient
      way to represent the internals of HTMLDefinition, and our
      implementation is by no means conforming and does not directly
      use the normative DTDs or XML schemas.
@note The public variables in a module should almost directly
      correspond to the variables in HTMLPurifier_HTMLDefinition.
      However, the prefix info carries no special meaning in these
      objects (include it anyway if that's the correspondence though).
@todo Consider making some member functions protected

## addElement()

Convenience function that sets up a new element
@param string $element Name of element to add
@param string|bool $type What content set should element be registered to?
             Set as false to skip this step.
@param string|HTMLPurifier_ChildDef $contents Allowed children in form of:
             "$content_model_type: $content_model"
@param array|string $attr_includes What attribute collections to register to
             element?
@param array $attr What unique attributes does the element define?
@see HTMLPurifier_ElementDef:: for in-depth descriptions of these parameters.
@return HTMLPurifier_ElementDef Created element definition object, so you
        can set advanced parameters

## addBlankElement()

Convenience function that creates a totally blank, non-standalone
element.
@param string $element Name of element to create
@return HTMLPurifier_ElementDef Created element

## addElementToContentSet()

Convenience function that registers an element to a content set
@param string $element Element to register
@param string $type Name content set (warning: case sensitive, usually upper-case
       first letter)

## parseContents()

Convenience function that transforms single-string contents
into separate content model and content model type
@param string $contents Allowed children in form of:
                 "$content_model_type: $content_model"
@return array
@note If contents is an object, an array of two nulls will be
      returned, and the callee needs to take the original $contents
      and use it directly.

## mergeInAttrIncludes()

Convenience function that merges a list of attribute includes into
an attribute array.
@param array $attr Reference to attr array to modify
@param array $attr_includes Array of includes / string include to merge in

## makeLookup()

Convenience function that generates a lookup table with boolean
true as value.
@param string $list List of values to turn into a lookup
@note You can also pass an arbitrary number of arguments in
      place of the regular argument
@return array array equivalent of list

## setup()

Lazy load construction of the module after determining whether
or not it's needed, and also when a finalized configuration object
is available.
@param HTMLPurifier_Config $config
