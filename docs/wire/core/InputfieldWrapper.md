# InputfieldWrapper

Source: `wire/core/InputfieldWrapper.php`

ProcessWire InputfieldWrapper

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

About InputfieldWrapper
=======================
A type of Inputfield that is designed specifically to wrap other Inputfields.
The most common example of an InputfieldWrapper is a <form>.

A type of Inputfield that contains other Inputfield objects as children. Commonly a form or a fieldset.

InputfieldWrapper is not designed to render an Inputfield specifically, but you can set a value attribute
containing content that will be rendered before the wrapper.

Access any common Inputfield type class name from an InputfieldWrapper and it will return a new instance of that Inputfield, i.e. `$f = $inputfields->InputfieldText;` Below are several examples.

## manipulation

@method Inputfield new($typeName, $name = '', $label = '', array $settings = [])

## output

@method string renderInputfield(Inputfield $inputfield, $renderValueMode = false)

## properties

@property InputfieldsArray|null $children Inputfield instances that are direct children of this InputfieldWrapper.

@property InputfieldAsmSelect $InputfieldAsmSelect Create new asmSelect Inputfield

@property InputfieldButton $InputfieldButton Create new button Inputfield

@property InputfieldCheckbox $InputfieldCheckbox Create new checkbox Inputfield

@property InputfieldCheckboxes $InputfieldCheckboxes Create new checkboxes Inputfield

@property InputfieldCKEditor $InputfieldCKEditor Create new CKEditor Inputfield

@property InputfieldDatetime $InputfieldDatetime Create new date/time Inputfield

@property InputfieldEmail $InputfieldEmail Create new email Inputfield

@property InputfieldFieldset $InputfieldFieldset Create new Fieldset InputfieldWrapper

@property InputfieldFile $InputfieldFile Create new file Inputfield

@property InputfieldFloat $InputfieldFloat Create new float Inputfield

@property InputfieldForm $InputfieldForm Create new form InputfieldWrapper

@property InputfieldHidden $InputfieldHidden Create new hidden Inputfield

@property InputfieldIcon $InputfieldIcon Create new icon Inputfield

@property InputfieldImage $InputfieldImage Create new image Inputfield

@property InputfieldInteger $InputfieldInteger Create new integer Inputfield

@property InputfieldMarkup $InputfieldMarkup Create new markup Inputfield

@property InputfieldPage $InputfieldPage Create new Page selection Inputfield

@property InputfieldPageAutocomplete $InputfieldPageAutocomplete Create new Page selection autocomplete Inputfield

@property InputfieldPageListSelect $InputfieldPageListSelect Create new PageListSelect Inputfield

@property InputfieldPageListSelectMultiple $InputfieldPageListSelectMultiple Create new multiple PageListSelect Inputfield

@property InputfieldRadios $InputfieldRadios Create new radio buttons Inputfield

@property InputfieldSelect $InputfieldSelect Create new <select> Inputfield

@property InputfieldSelectMultiple $InputfieldSelectMultiple Create new <select multiple> Inputfield

@property InputfieldSubmit $InputfieldSubmit Create new submit button Inputfield

@property InputfieldText $InputfieldText Create new single-line text Inputfield

@property InputfieldTextarea $InputfieldTextarea Create new multi-line <textarea> Inputfield

@property InputfieldTextTags $InputfieldTextTags Create new text tags Inputfield

@property InputfieldToggle $InputfieldToggle Create new toggle Inputfield

@property InputfieldURL $InputfieldURL Create new URL Inputfield

@property InputfieldWrapper $InputfieldWrapper Create new generic InputfieldWrapper

## __construct()

Construct the Inputfield, setting defaults for all properties

## wired()

Wired to API

## get()

Get a child Inputfield having a name attribute matching the given $key.

This method can also get settings, attributes or API variables, so long as they don't
collide with an Inputfield name. For that reason, you may prefer to use the `Inputfield::getSetting()`,
`Inputfield::attr()` or `Wire::wire()` methods for those other purposes.

If you want a method that can only return a matching Inputfield object, use the
`InputfieldWrapper::getChildByName()` method .


@param string $key Name of Inputfield or setting/property to retrieve.

@return Inputfield|mixed

@see InputfieldWrapper::getChildByName()

@throws WireException Only in core development/debugging, otherwise does not throw exceptions.

## __get()

Provides direct reference to attributes and settings, and falls back to Inputfield children

This is different behavior from the get() method.

@param string $key

@return mixed|null

## add()

Add an Inputfield item as a child (also accepts array definition)

Since 3.0.110: If given a string value, it is assumed to be an Inputfield type that you
want to add. In that case, it will create the Inputfield and return it instead of $this.


@param Inputfield|array|string $item

@return Inputfield|InputfieldWrapper|$this

@see InputfieldWrapper::import()

## ___new()

Create a new Inputfield, add it to this InputfieldWrapper, and return the new Inputfield

- Only the $typeName argument is required.
- You may optionally substitute the $settings argument for the $name or $label arguments.
- You may optionally substitute Inputfield “description” property for $settings argument.


@param string $typeName Inputfield type, i.e. “InputfieldCheckbox” or just “checkbox” for short.

@param string|array $name Name of input (or substitute $settings here).

@param string|array $label Label for input (or substitute $settings here).

@param array|string $settings Settings to add to Inputfield (optional). Or if string, assumed to be “description”.

@return Inputfield|InputfieldSelect|InputfieldWrapper An Inputfield instance ready to populate with additional properties/attributes.

@throws WireException If you request an unknown Inputfield type

@since 3.0.110

## import()

Import the given Inputfield items as children

If given an `InputfieldWrapper`, it will import the children of it and
exclude the wrapper itself. This is different from `InputfieldWrapper::add()`
in that add() would add the wrapper, not just the children. See also
the `InputfieldWrapper::importArray()` method.


@param InputfieldWrapper|array|InputfieldsArray $items Wrapper containing items to add

@return $this

@throws WireException

@see InputfieldWrapper::add(), InputfieldWrapper::importArray()

## prepend()

Prepend an Inputfield to this instance’s children.


@param Inputfield $item Item to prepend

@return $this

## append()

Append an Inputfield to this instance’s children.


@param Inputfield $item Item to append

@return $this

## insert()

Insert new or existing Inputfield before or after another


@param Inputfield|array|string $item New or existing item Inputfield, name, or new item array to insert.

@param Inputfield|string $existingItem Existing item or item name you want to insert before.

@param bool $before True to insert before, false to insert after (default=false).

@return $this

@throws WireException

@since 3.0.196

## insertBefore()

Insert one Inputfield before one that’s already there.

Note: string or array values for either argument require 3.0.196+.

~~~~~
// example 1: Get existing Inputfields and insert first_name before last_name
$firstName = $form->getByName('first_name');
$lastName = $form->getByName('last_name');
$form->insertBefore($firstName, $lastName);

// example 2: Same as above but use Inputfield names (3.0.196+)
$form->insertBefore('first_name', 'last_name');

// example 3: Create new Inputfield and insert before last_name (3.0.196+)
$form->insertBefore([ 'type' => 'text', 'name' => 'first_name' ], 'last_name');
~~~~~


@param Inputfield|array|string $item Item to insert

@param Inputfield|string $existingItem Existing item you want to insert before.

@return $this

## insertAfter()

Insert one Inputfield after one that’s already there.

Note: string or array values for either argument require 3.0.196+.

~~~~~
// example 1: Get existing Inputfields, insert last_name after first_name
$lastName = $form->getByName('last_name');
$firstName = $form->getByName('first_name');
$form->insertAfter($lastName, $firstName);

// example 2: Same as above but use Inputfield names (3.0.196+)
$form->insertBefore('last_name', 'first_name');

// example 3: Create new Inputfield and insert after first_name (3.0.196+)
$form->insertAfter([ 'type' => 'text', 'name' => 'last_name' ], 'first_name');
~~~~~


@param Inputfield|array|string $item Item to insert

@param Inputfield|string $existingItem Existing item you want to insert after.

@return $this

## remove()

Remove an Inputfield from this instance’s children.


@param Inputfield|string $key Inputfield object or name

@return $this

## removeByName()

Remove an Inputfield from the form by name

Note that this works the same as the getByName/getChildByName methods in that it
will find (and remove) the field by name, even if nested within other wrappers
or fieldsets. It returns the removed Inputfield when found, or null if not.

@param string $name

@return Inputfield|null Removed Inputfield object on success, or null if not found

@since 3.0.250

## preRenderChildren()

Prepare children for rendering by creating any fieldset groups

## classParents()

Get array of parent Inputfield classes for given Inputfield (excluding the base Inputfield class)

@param Inputfield|string $inputfield

@return array

## ___render()

Render this Inputfield and the output of its children.


@todo this method has become too long/complex, move to its own pluggable class and split it up a lot

@return string

## setAttributeInMarkup()

Set attribute value in markup, optionally replacing a {placeholder} tag

When a placeholder is present in the given $markup, it should be the
attribute name wrapped in `{}`, i.e. `{class}`

Note that class attributes are appended while other attributes are replaced.

@param string $name Attribute name (i.e. "class", "for", etc.)

@param string $value Value to set for the attribute

@param string $markup Markup where the attribute or placeholder exists

@param bool $removeEmpty Remove attribute if it resolves to empty value?

@return string Updated markup

@since 3.0.242

## removeAttributeFromMarkup()

Remove named attribute from given markup

@param string $name

@param string $markup

@return string

@since 3.0.250

## renderHeaderActions()

Render Inputfield header actions

@param Inputfield $inputfield

@param array $actions

@return string

@since 3.0.240

## ___renderValue()

Render the output of this Inputfield and its children, showing values only (no inputs)


@return string

## ___renderInputfield()

Render output for an individual Inputfield

This method takes care of all the pre-and-post requisites needed for rendering an Inputfield
among a group of Inputfields. It is used by the `InputfieldWrapper::render()` method for each
Inputfield present in the children.


@param Inputfield $inputfield The Inputfield to render.

@param bool $renderValueMode Specify true if we are only rendering values (default=false).

@return string Rendered output

## renderInputfieldAjaxPlaceholder()

Render a placeholder for an ajax-loaded Inputfield

@param Inputfield $inputfield

@param bool $renderValueMode

@return string

## ___processInput()

Process input for all children


@param WireInputData $input

@return $this

## isEmpty()

Returns true if all children are empty, or false if one or more is populated


@return bool

## getErrors()

Return an array of errors that occurred on any of the children during input processing.

Should only be called after `InputfieldWrapper::processInput()`.


@param bool $clear Specify true to clear out the errors (default=false).

@return array Array of error strings

## getErrorInputfields()

Get Inputfield objects that have errors


@return array|Inputfield[] Array of Inputfield objects indexed by Inputfield name attribute

@since 3.0.205

## children()

Return all children Inputfield objects


@param string $selector Optional selector string to filter the children by

@return InputfieldsArray

## child()

Find an Inputfield below this one that has the given name

This is an alternative to the `getChildByName()` method, with more options for when you need it.
For instance, it can also accept a selector string or numeric index for the $name argument, and you
can optionally disable the $recursive behavior.


@param string|int $name Name or selector string of child to find, omit for first child, or specify zero-based index of child to return.

@param bool $recursive Find child recursively? Looks for child in this wrapper, and all other wrappers below it. (default=true)

@return Inputfield|null Returns Inputfield instance if found, or null if not.

@since 3.0.110

## find()

Find all children Inputfields matching a selector string


@param string $selector Required selector string to filter the children by

@return InputfieldsArray

## getChildByName()

Given an Inputfield name, return the child Inputfield or NULL if not found.

This traverses all children recursively to find the requested Inputfield.

This is the same as the `InputfieldWrapper::get()` method except that it can
only return Inputfield or null, and has no crossover with other settings,
properties or API variables.


@param string $name Name of Inputfield

@return Inputfield|InputfieldWrapper|null

@see InputfieldWrapper::get(), InputfieldWrapper::children()

## getByName()

Shorter alias of getChildByName()


@param string $name

@return Inputfield|InputfieldWrapper|null

@since 3.0.172

## getByAttr()

Given an attribute name and value, return the first matching Inputfield or null if not found

This traverses all children recursively to find the requested Inputfield.


@param string $attrName Attribute to match, such as 'id', 'name', 'value', etc.

@param string $attrValue Attribute value to match

@return Inputfield|InputfieldWrapper|null

@since 3.0.196

## getByField()

Get Inputfield by Field (hasField)

This is useful in cases where the input name may differ from the Field name
that it represents, and you only know the field name. Applies only to
Inputfields connected with a Page and Field (i.e. used for page editing).


@param Field|string|int $field

@return Inputfield|InputfieldWrapper|null

@since 3.0.239

## getByProperty()

Get Inputfield by some other non-attribute property or setting


@param string $property

@param mixed $value

@param bool $getAll Get array of all matching Inputfields rather than just first? (default=false)

@return Inputfield|InputfieldWrapper|null|array

@since 3.0.239

## getValueByName()

Get value of Inputfield by name

This traverses all children recursively to find the requested Inputfield,
and get the value attribute from it. A value of null is returned if the
Inputfield cannot be found.

@param string $name

@return array|float|int|object|Wire|WireArray|WireData|string|null

@since 3.0.172

## getIterator()

Enables foreach() of the children of this class

Per the InteratorAggregate interface, make the Inputfield children iterable.


@return InputfieldsArray

## count()

Return the quantity of children present


@return int

## getAll()

Get all Inputfields below this recursively in a flat InputfieldWrapper (children, and their children, etc.)

Note that all InputfieldWrapper instances are removed as a result (except for the containing InputfieldWrapper).


@param array $options Options to modify behavior (3.0.169+)
 - `withWrappers` (bool): Also include InputfieldWrapper objects? (default=false) 3.0.169+

@return InputfieldsArray

## ___getConfigInputfields()

Get configuration Inputfields for this InputfieldWrapper


@return InputfieldWrapper

## importArray()

Import an array of Inputfield definitions to to this InputfieldWrapper instance

Your array should be an array of associative arrays, with each element describing an Inputfield.
The following properties are required for each Inputfield definition:

- `type` Which Inputfield module to use (may optionally exclude the "Inputfield" prefix).
- `name` Name attribute to use for the Inputfield.
- `label` Text label that appears above the Inputfield.

~~~~~
// Example array for Inputfield definitions
array(
  array(
    'name' => 'fullname',
    'type' => 'text',
    'label' => 'Field label'
    'columnWidth' => 50,
    'required' => true,
  ),
  array(
    'name' => 'color',
    'type' => 'select',
    'label' => 'Your favorite color',
    'description' => 'Select your favorite color or leave blank if you do not have one.',
    'columnWidth' => 50,
    'options' => array(
       'red' => 'Brilliant Red',
       'orange' => 'Citrus Orange',
       'blue' => 'Sky Blue'
    )
  ),
  // alternative usage: associative array where name attribute is specified as key
  'my_fieldset' => array(
    'type' => 'fieldset',
    'label' => 'My Fieldset',
    'children' => array(
      'some_field' => array(
        'type' => 'text',
        'label' => 'Some Field',
      )
    )
);
// Note: you may alternatively use associative arrays where the keys are assumed to
// be the 'name' attribute.See the last item 'my_fieldset' above for an example.
~~~~~


@param array $a Array of Inputfield definitions

@param InputfieldWrapper|null $inputfields Specify the wrapper you want them added to, or omit to use current.

@return $this

## populateValues()

Populate values for all Inputfields in this wrapper from the given $data object or array.

This iterates through every field in this InputfieldWrapper and looks for field names
that are also present in the given object or array. If present, it uses them to populate
the associated Inputfield.

If given an array, it should be an associative with the field 'name' as the keys and
the field 'value' as the array value, i.e. `['field_name' => 'field_value']`.


@param WireData|Wire|ConfigurableModule|array $data

@return array Returns array of field names that were populated
