# HTMLPurifier_DoctypeRegistry

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## get()

Retrieves reference to a doctype of a certain name
@note This function resolves aliases
@note When possible, use the more fully-featured make()
@param string $doctype Name of doctype
@return HTMLPurifier_Doctype Editable doctype object

## make()

Creates a doctype based on a configuration object,
will perform initialization on the doctype
@note Use this function to get a copy of doctype that config
      can hold on to (this is necessary in order to tell
      Generator whether or not the current document is XML
      based or not).
@param HTMLPurifier_Config $config
@return HTMLPurifier_Doctype

## getDoctypeFromConfig()

Retrieves the doctype from the configuration object
@param HTMLPurifier_Config $config
@return string
