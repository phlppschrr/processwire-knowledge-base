# HTMLPurifier_CSSDefinition

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Defines allowed CSS attributes and what their values are.
@see HTMLPurifier_HTMLDefinition

## doSetupProprietary()

@param HTMLPurifier_Config $config

## doSetupTricky()

@param HTMLPurifier_Config $config

## doSetupTrusted()

@param HTMLPurifier_Config $config

## setupConfigStuff()

Performs extra config-based processing. Based off of
HTMLPurifier_HTMLDefinition.
@param HTMLPurifier_Config $config
@todo Refactor duplicate elements into common class (probably using
      composition, not inheritance).
