# Inputfield

Source: `wire/core/Inputfield.php`

ProcessWire Inputfield - base class for Inputfield modules.

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

An Inputfield for an actual form input field widget, and this is provided as the base class
for different kinds of form input widgets provided as modules.

The class supports a parent/child hierarchy so that a given Inputfield can contain Inputfields
below it. An example would be the relationship between fieldsets and fields in a form.
Parent Inputfields are almost always of type InputfieldWrapper.

An Inputfield is typically associated with a Fieldtype module when used for ProcessWire fields.
Most Inputfields can also be used on their own.

Inputfield is the base class for modules that collect user input for fields.
These properties are retrieved or manipulated via the attribute methods above.
Constants for formats allowed in description, notes, label.
Constants allowed for the `Inputfield::collapsed` property.
Constants allowed for the `Inputfield::skipLabel` property.
Options for `Inputfield::renderValueFlags` property, applicable `Inputfield::renderValue()` method call.
Methods primarily of interest during module development.
Settings for Inputfields recognized and used by AdminThemeUikit.

~~~~~
// Create an Inputfield
$inputfield = $modules->get('InputfieldText');
$inputfield->label = 'Your Name';
$inputfield->attr('name', 'your_name');
$inputfield->attr('value', 'Roderigo');
// Add to a $form (InputfieldForm or InputfieldWrapper)
$form->add($inputfield);
~~~~~

ATTRIBUTES
==========

@property string $name HTML 'name' attribute for Inputfield (required).

@property string $id HTML 'id' attribute for the Inputfield (if not yet, determined automatically).

@property mixed $value HTML 'value' attribute for the Inputfield.

@property string $class HTML 'class' attribute for the Inputfield.

@method string|Inputfield name($name = null) Get or set the name attribute. @since 3.0.110

@method string|Inputfield id($id = null) Get or set the id attribute. @since 3.0.110

@method string|Inputfield class($class = null) Get class attribute or add a class to the class attribute. @since 3.0.110

LABELS & CONTENT
================

@property string $label Primary label text that appears above the input.

@property string $description Optional description that appears under label to provide more detailed information.

@property string $notes Optional notes that appear under input area to provide additional notes.

@property string $detail Optional text details that appear under notes. @since 3.0.140

@property string $icon Optional font-awesome icon name to accompany label (excluding the "fa-") part).

@property string $requiredLabel Optional custom label to display when missing required value. @since 3.0.98

@property string $tabLabel Label for tab if Inputfield rendered in its own tab via Inputfield::collapsedTab* setting. @since 3.0.201

@property string|null $prependMarkup Optional markup to prepend to the Inputfield content container.

@property string|null $appendMarkup Optional markup to append to the Inputfield content container.

@property string|null $footerMarkup Optional markup to add to the '.Inputfield' container, after '.InputfieldContent'. @since 3.0.241

@method string|Inputfield label($label = null) Get or set the 'label' property via method. @since 3.0.110

@method string|Inputfield description($description = null) Get or set the 'description' property via method. @since 3.0.110

@method string|Inputfield notes($notes = null) Get or set the 'notes' property via method. @since 3.0.110

@method string|Inputfield icon($icon = null) Get or set the 'icon' property via method. @since 3.0.110

@method string|Inputfield requiredLabel($requiredLabel = null) Get or set the 'requiredLabel' property via method. @since 3.0.110

@method string|Inputfield head($head = null) Get or set the 'head' property via method. @since 3.0.110

@method string|Inputfield prependMarkup($markup = null) Get or set the 'prependMarkup' property via method. @since 3.0.110

@method string|Inputfield appendMarkup($markup = null) Get or set the 'appendMarkup' property via method. @since 3.0.110

APPEARANCE
==========

@property int $collapsed Whether the field is collapsed or visible, using one of the "collapsed" constants.

@property string $showIf Optional conditions under which the Inputfield appears in the form (selector string).

@property int $columnWidth Width of column for this Inputfield 10-100 percent. 0 is assumed to be 100 (default).

@property int $skipLabel Skip display of the label? See the "skipLabel" constants for options.

@method int|Inputfield collapsed($collapsed = null) Get or set collapsed property via method. @since 3.0.110

@method string|Inputfield showIf($showIf = null) Get or set showIf selector property via method. @since 3.0.110

@method int|Inputfield columnWidth($columnWidth = null) Get or set columnWidth property via method. @since 3.0.110

@method int|Inputfield skipLabel($skipLabel = null) Get or set the skipLabel constant property via method. @since 3.0.110

UIKIT THEME
===========

@property bool|string $themeOffset Offset/margin for Inputfield, one of 's', 'm', or 'l'.

@property string $themeBorder Border style for Inputfield, one of 'none', 'card', 'hide' or 'line'.

@property string $themeInputSize Input size height/font within Inputfield, one of 's', 'm', or 'l'.

@property string $themeInputWidth Input width for text-type inputs, one of 'xs', 's', 'm', 'l', or 'f' (for full-width).

@property string $themeColor Color theme for Inputfield, one of 'primary', 'secondary', 'warning', 'danger', 'success', 'highlight', 'none'.

@property bool $themeBlank Makes <input> element display with no minimal container / no border when true.

SETTINGS & BEHAVIOR
===================

@property int|bool $required Set to true (or 1) to make input required, or false (or 0) to make not required (default=0).

@property string $requiredIf Optional conditions under which input is required (selector string).

@property int|bool|null $requiredAttr Use HTML5 “required” attribute when used by Inputfield and $required is true? Default=null.

@property null|bool|Fieldtype $hasFieldtype The Fieldtype using this Inputfield, or boolean false when known not to have a Fieldtype, or null when not known.

@property null|Field $hasField The Field object associated with this Inputfield, or null when not applicable or not known.

@property null|Page $hasPage The Page object associated with this Inputfield, or null when not applicable or not known.

@property null|Inputfield $hasInputfield If this Inputfield is owned/managed by another (other than parent/child relationship), it may be set here. @since 3.0.176

@property bool|null $useLanguages When multi-language support active, can be set to true to make it provide inputs for each language, where supported (default=false).

@property null|bool|int $entityEncodeLabel Set to boolean false to specifically disable entity encoding of field header/label (default=true).

@property null|bool $entityEncodeText Set to boolean false to specifically disable entity encoding for other text: description, notes, etc. (default=true).

@property int $renderFlags Options that can be applied to render, see "render*" constants (default=0). @since 3.0.204

@property int $renderValueFlags Options that can be applied to renderValue mode, see "renderValue" constants (default=0).

@property string $wrapClass Optional class name (CSS) to apply to the HTML element wrapping the Inputfield.

@property string $headerClass Optional class name (CSS) to apply to the InputfieldHeader element

@property string $contentClass Optional class name (CSS) to apply to the InputfieldContent element

@property string $addClass Formatted class string letting you add class to any of the above (see addClass method). @since 3.0.204

@property int|null $textFormat Text format to use for description/notes text in Inputfield (see textFormat constants)

@method string|Inputfield required($required = null) Get or set required state. @since 3.0.110

@method string|Inputfield requiredIf($requiredIf = null) Get or set required-if selector. @since 3.0.110

@method string|Inputfield wrapClass($class = null) Get wrapper class attribute or add a class to it. @since 3.0.110

@method string|Inputfield headerClass($class = null) Get header class attribute or add a class to it. @since 3.0.110

@method string|Inputfield contentClass($class = null) Get content class attribute or add a class to it. @since 3.0.110

MULTI-LANGUAGE METHODS (requires LanguageSupport module to be installed)
======================

@method void setLanguageValue($language, $value) Set language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238

@method string|mixed getLanguageValue($language) Get language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238

HOOKABLE METHODS
================

@method string render()

@method string renderValue()

@method void renderReadyHook(Inputfield $parent, $renderValueMode)

@method Inputfield processInput(WireInputData $input)

@method InputfieldWrapper getConfigInputfields()

@method array getConfigArray()

@method array getConfigAllowContext(Field $field)

## collapsedNo

Not collapsed (display as "open", default)

## collapsedYes

Collapsed unless opened

## collapsedBlank

Collapsed only when blank

## collapsedHidden

Hidden, not rendered in the form at all

## collapsedPopulated

Collapsed only when populated

## collapsedNoLocked

Not collapsed, value visible but not editable

## collapsedBlankLocked

Collapsed when blank, value visible but not editable

## collapsedYesLocked

Collapsed unless opened (value becomes visible but not editable)

## collapsedNever

Never collapsed, and not collapsible

## collapsedYesAjax

Collapsed and dynamically loaded by AJAX when opened

## collapsedBlankAjax

Collapsed only when blank, and dynamically loaded by AJAX when opened

## collapsedTab

Collapsed into a separate tab

@since 3.0.201

## collapsedTabAjax

Collapsed into a separate tab and AJAX loaded

@since 3.0.201

## collapsedTabLocked

Collapsed into a separate tab and locked (not editable)

@since 3.0.201

## skipLabelNo

Don't skip the label (default)

## skipLabelFor

Don't use a "for" attribute with the <label>

## skipLabelHeader

Don't show a visible header (likewise, do not show the label)

## skipLabelBlank

Skip rendering of the label when it is blank

## skipLabelMarkup

Do not render any markup for the header/label at all

@since 3.0.139

## textFormatNone

Plain text: no type of markdown or HTML allowed

## textFormatBasic

Only allow basic/inline markdown, and no HTML (default)

## textFormatMarkdown

Full markdown support with HTML also allowed

## renderFirst

Render flags: place first in render

## renderLast

Render flags: place last in render

## renderValueMinimal

Render only the minimum output when in "renderValue" mode.

## renderValueNoWrap

Indicates a parent InputfieldWrapper is not required when rendering value.

## renderValueFirst

If there are multiple items, only render the first (where supported by the Inputfield).

## __construct()

Construct the Inputfield, setting defaults for all properties

## init()

Per the Module interface, init() is called after any configuration data has been populated to the Inputfield, but before render.

## ___install()

Per the Module interface, this method is called when this Inputfield is installed

## ___uninstall()

Per the Module interface, uninstall() is called when this Inputfield is uninstalled

## set()

Set a property or attribute to the Inputfield

- Use this for setting properties like parent, collapsed, required, columnWidth, etc.
- You can also set properties directly via `$inputfield->property = $value`.
- If setting an attribute (like name, id, etc.) this will work, but it is preferable to use the `Inputfield::attr()` method.
- If setting any kind of "class" it is preferable to use the `Inputfield::addClass()` method.


@param string $key Name of property to set

@param mixed $value Value of property

@return Inputfield|WireData

## get()

Get a property or attribute from the Inputfield

- This can also be accessed directly, i.e. `$value = $inputfield->property;`.

- For getting attribute values, this will work, but it is preferable to use the `Inputfield::attr()` method.

- For getting non-attribute values that have potential name conflicts with attributes (or just as a
  reliable alternative), use the `Inputfield::getSetting()` method instead, which excludes the possibility
  of overlap with attributes.


@param string $key Name of property or attribute to retrieve.

@return mixed|null Value of property or attribute, or NULL if not found.

## getSetting()

Gets a setting (or API variable) from the Inputfield, while ignoring attributes.

This is good to use in cases where there are potential name conflicts, like when there is a field literally
named "collapsed" or "required".


@param string $key Name of setting or API variable to retrieve.

@return mixed Value of setting or API variable, or NULL if not found.

## setParent()

Set the parent (InputfieldWrapper) of this Inputfield.


@param InputfieldWrapper $parent

@return $this

@see Inputfield::getParent()

## getParent()

Get this Inputfield’s parent InputfieldWrapper, or NULL if it doesn’t have one.


@return InputfieldWrapper|null

@see Inputfield::setParent()

## getParents()

Get array of all parents of this Inputfield.


@return array of InputfieldWrapper elements.

@see Inputfield::getParent(), Inputfield::setParent()

## parent()

Get or set parent of Inputfield

This convenience method performs the same thing as getParent() and setParent().

To get parent, specify no arguments. It will return null if no parent assigned, or an
InputfieldWrapper instance of the parent.

To set parent, specify an InputfieldWrapper for the $parent argument. The return value
is the current Inputfield for fluent interface.


@param null|InputfieldWrapper $parent

@return null|Inputfield|InputfieldWrapper

@since 3.0.110

## parents()

Get array of all parents of this Inputfield

This is identical to and an alias of the getParents() method.


@return array

@since 3.0.110

## getRootParent()

Get the root parent InputfieldWrapper element (farthest parent, commonly InputfieldForm)

This returns null only if Inputfield it is called from has not yet been added to an InputfieldWrapper.


@return InputfieldForm|InputfieldWrapper|null

@since 3.0.106

## getForm()

Get the InputfieldForm element that contains this field or null if not yet defined

This is the same as the `getRootParent()` method except that it returns null if root parent
is not an InputfieldForm.


@return InputfieldForm|null

@since 3.0.106

## removeAttr()

Remove an attribute


@param string $key Name of attribute to remove.

@return $this

@see Inputfield::attr(), Inputfield::removeClass()

## attr()

Get or set an attribute (or multiple attributes)

- To get an attribute call this method with just the attribute name.
- To set an attribute call this method with the attribute name and value to set.
- You can also set multiple attributes at once, see examples below.
- To get all attributes, just specify boolean true as first argument (since 3.0.16).

~~~~~
// Get the "value" attribute
$value = $inputfield->attr('value');

// Set the "value" attribute
$inputfield->attr('value', 'Foo and Bar');

// Set multiple attributes
$inputfield->attr([
  'name' => 'foobar',
  'value' => 'Foo and Bar',
  'class' => 'foo-bar',
]);

// Set name and id attribute to "foobar"
$inputfield->attr("name+id", "foobar");

// Get all attributes in associative array (since 3.0.16)
$attrs = $inputfield->attr(true);
~~~~~


@param string|array|bool $key Specify one of the following:
  - Name of attribute to get (if getting an attribute).
  - Name of attribute to set (if setting an attribute, and also specifying a value).
  - Aassociative array to set multiple attributes.
  - String with attributes split by "+" or "|" to set them all to have the same value.
  - Specify boolean true to get all attributes in an associative array.

@param string|int|bool|null $value Value to set (if setting), omit otherwise.

@return Inputfield|array|string|int|object|float If setting an attribute, it returns this instance. If getting an attribute, the attribute is returned.

@see Inputfield::removeAttr(), Inputfield::addClass(), Inputfield::removeClass()

## val()

Shortcut for getting or setting “value” attribute

When setting a value, it returns $this (for fluent interface).

~~~~~
$value = $inputfield->val(); * // Getting
$inputfield->val('foo'); * // Setting
~~~~~

@param string|null $value

@return string|int|float|array|object|Wire|WireData|WireArray|Inputfield

## wrapAttr()

Get or set attribute for the element wrapping this Inputfield

Use this method when you need to assign some attribute to the outer wrapper of the Inputfield.


@param string|null|bool $key Specify one of the following for $key:
  - Specify string containing name of attribute to set.
  - Omit (or null or true) to get all wrap attributes as associative array.

@param string|null|bool $value Specify one of the following for $value:
  - Omit if getting an attribute.
  - Value to set for $key of setting.
  - Boolean false to remove the attribute specified for $key.

@return Inputfield|string|array|null Returns one of the following:
  - If getting, returns attribute value of NULL if not present.
  - If setting, returns $this.

@see Inputfield::attr(), Inputfield::addClass()

## addClass()

Add a class or classes to this Inputfield (or a wrapping element)

If given a class name that’s already present, it won’t be added again.

~~~~~
// Add class "foobar" to input element
$inputfield->addClass('foobar');

// Add three classes to input element
$inputfield->addClass('foo bar baz');

// Add class "foobar" to .Inputfield wrapping element
$inputfield->addClass('foobar', 'wrapClass');

// Add classes while specifying Inputfield element (3.0.204+)
$inputfield->addClass('wrap:card, header:card-header, content:card-body');
~~~~~

**Formatted string option (3.0.204+):**
Classes can be added by formatted string that dictates what Inputfield element they
should be added to, in the format `element:classNames` like in this example below:
~~~~~
wrap:card card-default
header:card-header
content:card-body
input:form-input input-checkbox
~~~~~
Each line represents a group containing an element name and one or more space-separated
classes. Groups may be separated by newline (like above) or with a comma. The element
name may be any one of the following:

 - `wrap`: The .Inputfield element that wraps the header and content
 - `header`: The .InputfieldHeader element, typically a `<label>`.
 - `content`: The .InputfieldContent element that wraps the input(s), typically a `<div>`.
 - `input`: The primary `<input>` element(s) that accept input for the Inputfield.
 - `class`: This is the same as the 'input' type, just an alias.

Class names prefixed with a minus sign i.e. `-class` will be removed rather than added.


@param string|array $class Specify one of the following:
  - Class name you want to add.
  - Multiple space-separated class names you want to add.
  - Array of class names you want to add (since 3.0.16).
  - Formatted string of classes as described in method description (since 3.0.204+).

@param string $property Optionally specify the type of class you want to add:
  - Omit for the default (which is "class").
  - `class` (string): Add class to the input element (or whatever the Inputfield default is).
  - `wrapClass` (string): Add class to ".Inputfield" wrapping element, the most outer level element used for this Inputfield.
  - `headerClass` (string): Add class to ".InputfieldHeader" label element.
  - `contentClass` (string): Add class to ".InputfieldContent" wrapping element.
  - Or some other named class attribute designated by a descending Inputfield.
  - You can optionally omit the `Class` suffix in 3.0.204+, i.e. `wrap` rather than `wrapClass`.

@return $this

@see Inputfield::hasClass(), Inputfield::removeClass()

## addClassString()

Add class(es) by formatted string that lets you specify where class should be added

To use this in the public API use `addClass()` method or set the `addClass` property
with a formatted string value as indicated here.

Allows for setting via formatted string like:
~~~~~
wrap:card card-default
header:card-header
content:card-body
input:form-input input-checkbox
~~~~~
Each line represents a group containing a element type, colon, and one or more space-
separated classes. Groups may be separated by newline (like above) or with a comma.
The element type may be any one of the following:

 - `wrap`: The .Inputfield element that wraps the header and content
 - `header`: The .InputfieldHeader element, typically a `<label>`.
 - `content`: The .InputfieldContent element that wraps the input(s), typically a `<div>`.
 - `input`: The primary `<input>` element(s) that accept input for the Inputfield.
 - `class`: This is the same as the 'input' type, just an alias.
 - `+foo`: Force adding your own new element type (i.e. “foo”) that is not indicated above.

Class names prefixed with a minus sign i.e. `-class` will be removed rather than added.

A string like `hello:world` where `hello` is not one of those element types listed above,
and is not prefixed with a plus sign `+`, will be added as a literal class name with the
colon in it (such as those used by Tailwind).

@param string $class Formatted class string to parse class types and names from

@param string $property Default/fallback element/property if not indicated in string

@return self

@since 3.0.204

## hasClass()

Does this Inputfield have the given class name (or names)?

~~~~~
if($inputfield->hasClass('foo')) {
  // This Inputfield has a class attribute with "foo"
}

if($inputfield->hasClass('bar', 'wrapClass')) {
  // This .Inputfield wrapper has a class attribute with "bar"
}

if($inputfield->hasClass('foo bar')) {
  // This Inputfield has both "foo" and "bar" classes (Since 3.0.16)
}
~~~~~


@param string|array $class Specify class name or one of the following:
  - String containing name of class you want to check (string).
  - String containing Space separated string class names you want to check, all must be present for
    this method to return true. (Since 3.0.16)
  - Array of class names you want to check, all must be present for this method to return true. (Since 3.0.16)

@param string $property Optionally specify property you want to pull class from:
  - `class` (string): Default setting. Class for the input element (or whatever the Inputfield default is).
  - `wrapClass` (string): Class for the ".Inputfield" wrapping element, the most outer level element used for this Inputfield.
  - `headerClass` (string): Class for the ".InputfieldHeader" label element.
  - `contentClass` (string): Class for the ".InputfieldContent" wrapping element.
  - Or some other class property defined by a descending Inputfield class.

@return bool

@see Inputfield::addClass(), Inputfield::removeClass()

## getClassArray()

Get classes in array for given class property

@param string $property One of 'wrap', 'header', 'content' or 'input' (or alias 'class')

@param bool $assoc Return as associative array where both keys and values are class names? (default=false)

@return array

@since 3.0.204

## getClassProperty()

Get the internal property name for given class property

This converts things like 'wrap' to 'wrapClass', 'header' to 'headerClass', etc.

@param string $property

@return string

@since 3.0.204

## removeClass()

Remove the given class (or classes) from this Inputfield

~~~~~
// Remove the "foo" class
$inputfield->removeClass('foo');

// Remove both the "foo" and "bar" classes (since 3.0.16)
$inputfield->removeClass('foo bar');

// Remove the "bar" class from the wrapping .Inputfield element
$inputfield->removeClass('bar', 'wrapClass');
~~~~~


@param string|array $class Class name you want to remove or specify one of the following:
  - Single class name to remove.
  - Space-separated class names you want to remove (Since 3.0.16).
  - Array of class names you want to remove (Since 3.0.16).

@param string $property Optionally specify the property you want to remove class from:
  - `class` (string): Default setting. Class for the input element (or whatever the Inputfield default is).
  - `wrapClass` (string): Class for the ".Inputfield" wrapping element, the most outer level element used for this Inputfield.
  - `headerClass` (string): Class for the ".InputfieldHeader" label element.
  - `contentClass` (string): Class for the ".InputfieldContent" wrapping element.
  - Or some other class property defined by a descending Inputfield class.

@return $this

@see Inputfield::addClass(), Inputfield::hasClass()

## ___render()

Render the HTML input element(s) markup, ready for insertion in an HTML form.

This is an abstract method that descending Inputfield module classes are required to implement.


@return string

## ___renderValue()

Render just the value (not input) in text/markup for presentation purposes.


@return string Text or markup where applicable

## renderReady()

Method called right before Inputfield markup is rendered, so that any dependencies can be loaded as well.

Called before `Inputfield::render()` or `Inputfield::renderValue()` method by the parent `InputfieldWrapper`
instance. If you are calling either of those methods yourself for some reason, make sure that you call this
`renderReady()` method first.

The default behavior of this method is to populate Inputfield-specific CSS and JS file assets into
`$config->styles` and `$config->scripts`.

The return value is true if assets were just added, and false if assets have already been added in a previous
call. This distinction probably doesn't matter in most usages, but here just in case a descending class needs
to know when/if to add additional assets (i.e. when this method returns true).


@param Inputfield|null The parent InputfieldWrapper that is rendering it, or null if no parent.

@param bool $renderValueMode Specify true only if this is for `Inputfield::renderValue()` rather than `Inputfield::render()`.

@return bool True if assets were just added, false if already added.

## ___renderReadyHook()

Hookable version of renderReady(), not called unless 'renderReadyHook' is hooked

Hook this method instead if you want to hook renderReady().

@param Inputfield|null $parent

@param bool $renderValueMode

## ___processInput()

Process input for this Inputfield directly from the POST (or GET) variables

This method should pull the value from the given `$input` argument, sanitize/validate it, and
populate it to the `value` attribute of this Inputfield.

Inputfield modules should implement this method if the built-in one here doesn't solve their need.
If this one does solve their need, then they should add any additional sanitization or validation
to the `Inputfield::setAttribute('value', $value)` method to occur when given the `value` attribute.


@param WireInputData $input User input where value should be pulled from (typically `$input->post`)

@return $this

## isEmpty()

Is this Inputfield empty? (Value attribute reflects an empty state)

Return true if this field is empty (no value or blank value), or false if it’s not empty.

Used by the 'required' check to see if the field is populated, and descending Inputfields may
override this according to their own definition of 'empty'.


@return bool

## ___getConfigInputfields()

Get any custom configuration fields for this Inputfield

- Intended to be extended by each Inputfield as needed to add more config options.

- The returned InputfieldWrapper ultimately ends up as the "Input" tab in the fields editor (admin).

- Descending Inputfield classes should first call this method from the parent class to get the
  default configuration fields and the InputfieldWrapper they can add to.

- Returned Inputfield instances with a name attribute that starts with an underscore, i.e. "_myname"
  are assumed to be for runtime use and are NOT stored in the database.

- If you prefer, you may instead implement the `Inputfield::getConfigArray()` method as an alternative.

~~~~
// Example getConfigInputfields() implementation
public function ___getConfigInputfields() {
  // Get the defaults and $inputfields wrapper we can add to
  $inputfields = parent::___getConfigInputfields();
  // Add a new Inputfield to it
  $f = $this->wire('modules')->get('InputfieldText');
  $f->attr('name', 'first_name');
  $f->attr('value', $this->get('first_name'));
  $f->label = 'Your First Name';
  $inputfields->add($f);
  return $inputfields;
}
~~~~


@return InputfieldWrapper Populated with Inputfield instances

@see Inputfield::getConfigArray()

## ___getConfigArray()

Alternative method for configuration that allows for array definition

- This method is typically used instead of the `Inputfield::getConfigInputfields` method
  for module authors that prefer to use the array definition.

- If both `getConfigInputfields()` and `getConfigArray()` are implemented, both will be used.

- See comments for `InputfieldWrapper::importArray()` for example of array definition.

~~~~~
// Example implementation
public function ___getConfigArray() {
  return [
    'test' => [
      'type' => 'text',
      'label' => 'This is a test',
      'value' => 'Test'
    ]
  ];
);
~~~~~


@return array

## ___getConfigAllowContext()

Return a list of config property names allowed for fieldgroup/template context

These should be the names of Inputfields returned by `Inputfield::getConfigInputfields()` or
`Inputfield::getConfigArray()` that are allowed in fieldgroup/template context.

The config property names specified here are allowed to be configured within the context
of a given `Fieldgroup`, enabling the user to configure them independently per template
in the admin.

This is the equivalent to the `Fieldtype::getConfigAllowContext()` method, but for the "Input"
tab rather than the "Details" tab.


@param Field $field

@return array of Inputfield names

@see Fieldtype::getConfigAllowContext()

## error()

Record an error for this Inputfield

The error message will be placed in the context of this Inputfield.
See the `Wire::error()` method for full details on arguments and options.


@param string $text Text of error message

@param int $flags Optional flags

@return $this

## getErrors()

Return array of strings containing errors that occurred during input processing

Note that this is different from `Wire::errors()` in that it retrieves errors from the session
rather than just the current run.


@param bool $clear Optionally clear the errors after getting them (Default=false).

@return array

## clearErrors()

Clear errors from this Inputfield

This is the same as `$inputfield->getErrors(true);` but has no return value.


@since 3.0.205

## has()

Does this Inputfield have the requested property or attribute?


@param string $key Requested property or attribute.

@return bool True if it has it, false if it doesn't

## entityEncode()

Entity encode a string with optional Markdown support.

- Markdown support provided with second argument.
- If string is already entity-encoded it will first be decoded.


@param string $str String to encode

@param bool|int $markdown Optionally specify one of the following:
  - `true` (boolean): To allow Markdown using default "textFormat" setting (which is basic Markdown by default).
  - `false` (boolean): To disallow Markdown support (this is the default when $markdown argument omitted).
  - `Inputfield::textFormatNone` (constant): Disallow Markdown support (default).
  - `Inputfield::textFormatBasic` (constant): To support basic/inline Markdown.
  - `Inputfield::textFormatMarkdown` (constant): To support full Markdown and HTML.

@return string Entity encoded string or HTML string

## editable()

Get or set editable state for this Inputfield

When set to false, the `Inputfield::processInput()` method won't be called by parent InputfieldWrapper,
effectively skipping over input processing entirely for this Inputfield.


@param bool|null $setEditable Specify true or false to set the editable state, or omit just to get the editable state.

@return bool Returns the current editable state.

## addHeaderAction()

Add header action

This adds a clickable icon to the right side of the Inputfield header.
There are three types of actions: 'click', 'toggle' and 'link'. The 'click'
action simply triggers your JS event whenever it is clicked. The 'toggle' action
has an on/off state, and you can specify the JS event to trigger for each.
This function will automatically figure out whether you want a `click`,
`toggle` or 'link' action based on what you provide in the $settings argument.
Below is a summary of these settings:

Settings for 'click' or 'link' type actions
-------------------------------------------
- `icon` (string): Name of font-awesome icon to use.
- `tooltip` (string): Optional tooltip text to display when icon hovered.
- `event` (string): Event name to trigger in JS when clicked ('click' actions only).
- `href` (string): URL to open ('link' actions only).
- `modal` (bool): Specify true to open link in modal ('link' actions only).
- `target` (string): Optional target attribute i.e. '_blank'.

Settings for 'toggle' (on/off) type actions
-------------------------------------------
- `on` (bool): Start with the 'on' state? (default=false)
- `onIcon` (string): Name of font-awesome icon to show for on state.
- `onEvent` (string): JS event name to trigger when toggled on.
- `onTooltip` (string): Tooltip text to show when on icon is hovered.
- `offIcon` (string): Name of font-awesome icon to show for off state.
- `offEvent` (string): JS event name to trigger when toggled off.
- `offTooltip` (string): Tooltip text to show when off icon is hovered.

Other/optional settings (applies to all types)
----------------------------------------------
- `name` (string): Name of this action (-_a-zA-Z0-9).
- `parent` (string): Name of parent action, if this action is part of a menu.
- `overIcon` (string): Name of font-awesome icon to show when hovered.
- `overEvent` (string): JS event name to trigger when mouse is over the icon.
- `downIcon` (string): Icon to display when mouse is down on the action icon (3.0.241+).
- `downEvent` (string): JS event name to trigger when mouse is down on the icon (3.0.241+).
- `cursor` (string): CSS cursor name to show when mouse is over the icon.
- `setAll` (array): Set all of the header actions in one call, replaces any existing.
   Note: to get all actions, call the method and omit the $settings argument.

Settings for dropdown menu actions (3.0.241+)
---------------------------------------------
 Note that menu type actions also require jQuery UI and /wire/templates-admin/scripts/main.js,
 both of which are already present in PW’s admin themes (AdminThemeUikit recommended).
 Requires ProcessWire 3.0.241 or newer.
 - `icon` (string): Icon name to use for dropdown toggle, i.e. 'fa-wrench'.
 - `tooltip` (string): Optional tooltip to describe what the dropdown is for.
 - `menuAction` (string): Action that toggles the menu to show, one of 'click' or 'hover' (default).
 - `menuItems` (array): Definition of menu items, each with one or more of the following properties.
    - `label` (string): Label text for the menu item (required).
    - `icon` (string): Icon name for the menu item, if desired.
    - `callback` (function|null): JS callback to execute item is clicked (not applicable in PHP).*
    - `event` (string): JS event name to trigger when item is clicked.
    - `tooltip` (string): Tooltip text to show when hovering menu item (title attribute).
    - `href` (string): URL to go to when menu item clicked.
    - `target` (string): Target attribute when href is used (i.e. "_blank").
    - `modal` (bool): Open href in modal window instead?
    - `active` (function|bool): Callback function that returns true if menu item active, or false.*
       if disabled. You can also directly specify true or false for this option.
    - NOTE 1: All `menuItems` properties above are optional, except for 'label'.
    - NOTE 2: To use `callback` or `active` as functions, you must define your menu in JS instead.
    - NOTE 3: For examples see the addHeaderAction() method in /wire/templates-admin/scripts/inputfields.js

@param array $settings Specify array containing the appropriate settings above.

@return array Returns all currently added actions.

@since 3.0.240

## __debugInfo()

debugInfo PHP 5.6+ magic method

@return array
