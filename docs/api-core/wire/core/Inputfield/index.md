# Inputfield

Source: `wire/core/Inputfield.php`

Inherits: `WireData`
Implements: `Module`

ProcessWire Inputfield - base class for Inputfield modules.


An Inputfield for an actual form input field widget, and this is provided as the base class
for different kinds of form input widgets provided as modules.

The class supports a parent/child hierarchy so that a given Inputfield can contain Inputfields
below it. An example would be the relationship between fieldsets and fields in a form.
Parent Inputfields are almost always of type InputfieldWrapper.

An Inputfield is typically associated with a Fieldtype module when used for ProcessWire fields.
Most Inputfields can also be used on their own.

Inputfield is the base class for modules that collect user input for fields.

~~~~~
// Create an Inputfield
$inputfield = $modules->get('InputfieldText');
$inputfield->label = 'Your Name';
$inputfield->attr('name', 'your_name');
$inputfield->attr('value', 'Roderigo');
// Add to a $form (InputfieldForm or InputfieldWrapper)
$form->add($inputfield);
~~~~~

## Attributes

- [`$name: string`](method-name.md) HTML 'name' attribute for Inputfield (required).
- [`$id: string`](method-id.md) HTML 'id' attribute for the Inputfield (if not yet, determined automatically).
- `$value: mixed` HTML 'value' attribute for the Inputfield.
- [`$class: string`](method-class.md) HTML 'class' attribute for the Inputfield.
- [`name($name = null): string|Inputfield`](method-name.md) Get or set the name attribute. @since 3.0.110
- [`id($id = null): string|Inputfield`](method-id.md) Get or set the id attribute. @since 3.0.110
- [`class($class = null): string|Inputfield`](method-class.md) Get class attribute or add a class to the class attribute. @since 3.0.110

## Labels & Content

- [`$label: string`](method-label.md) Primary label text that appears above the input.
- [`$description: string`](method-description.md) Optional description that appears under label to provide more detailed information.
- [`$notes: string`](method-notes.md) Optional notes that appear under input area to provide additional notes.
- `$detail: string` Optional text details that appear under notes. @since 3.0.140
- [`$icon: string`](method-icon.md) Optional font-awesome icon name to accompany label (excluding the "fa-") part).
- [`$requiredLabel: string`](method-requiredlabel.md) Optional custom label to display when missing required value. @since 3.0.98
- `$tabLabel: string` Label for tab if Inputfield rendered in its own tab via Inputfield::collapsedTab* setting. @since 3.0.201
- [`$prependMarkup: string|null`](method-prependmarkup.md) Optional markup to prepend to the Inputfield content container.
- [`$appendMarkup: string|null`](method-appendmarkup.md) Optional markup to append to the Inputfield content container.
- `$footerMarkup: string|null` Optional markup to add to the '.Inputfield' container, after '.InputfieldContent'. @since 3.0.241
- [`label($label = null): string|Inputfield`](method-label.md) Get or set the 'label' property via method. @since 3.0.110
- [`description($description = null): string|Inputfield`](method-description.md) Get or set the 'description' property via method. @since 3.0.110
- [`notes($notes = null): string|Inputfield`](method-notes.md) Get or set the 'notes' property via method. @since 3.0.110
- [`icon($icon = null): string|Inputfield`](method-icon.md) Get or set the 'icon' property via method. @since 3.0.110
- [`requiredLabel($requiredLabel = null): string|Inputfield`](method-requiredlabel.md) Get or set the 'requiredLabel' property via method. @since 3.0.110
- [`head($head = null): string|Inputfield`](method-head.md) Get or set the 'head' property via method. @since 3.0.110
- [`prependMarkup($markup = null): string|Inputfield`](method-prependmarkup.md) Get or set the 'prependMarkup' property via method. @since 3.0.110
- [`appendMarkup($markup = null): string|Inputfield`](method-appendmarkup.md) Get or set the 'appendMarkup' property via method. @since 3.0.110

## Appearance

- [`$collapsed: int`](method-collapsed.md) Whether the field is collapsed or visible, using one of the "collapsed" constants.
- [`$showIf: string`](method-showif.md) Optional conditions under which the Inputfield appears in the form (selector string).
- [`$columnWidth: int`](method-columnwidth.md) Width of column for this Inputfield 10-100 percent. 0 is assumed to be 100 (default).
- [`$skipLabel: int`](method-skiplabel.md) Skip display of the label? See the "skipLabel" constants for options.
- [`collapsed($collapsed = null): int|Inputfield`](method-collapsed.md) Get or set collapsed property via method. @since 3.0.110
- [`showIf($showIf = null): string|Inputfield`](method-showif.md) Get or set showIf selector property via method. @since 3.0.110
- [`columnWidth($columnWidth = null): int|Inputfield`](method-columnwidth.md) Get or set columnWidth property via method. @since 3.0.110
- [`skipLabel($skipLabel = null): int|Inputfield`](method-skiplabel.md) Get or set the skipLabel constant property via method. @since 3.0.110

## Uikit Theme

- `$themeOffset: bool|string` Offset/margin for Inputfield, one of 's', 'm', or 'l'.
- `$themeBorder: string` Border style for Inputfield, one of 'none', 'card', 'hide' or 'line'.
- `$themeInputSize: string` Input size height/font within Inputfield, one of 's', 'm', or 'l'.
- `$themeInputWidth: string` Input width for text-type inputs, one of 'xs', 's', 'm', 'l', or 'f' (for full-width).
- `$themeColor: string` Color theme for Inputfield, one of 'primary', 'secondary', 'warning', 'danger', 'success', 'highlight', 'none'.
- `$themeBlank: bool` Makes <input> element display with no minimal container / no border when true.

## Settings & Behavior

- [`$required: int|bool`](method-required.md) Set to true (or 1) to make input required, or false (or 0) to make not required (default=0).
- [`$requiredIf: string`](method-requiredif.md) Optional conditions under which input is required (selector string).
- `$requiredAttr: int|bool|null` Use HTML5 “required” attribute when used by Inputfield and $required is true? Default=null.
- `$hasFieldtype: null|bool|Fieldtype` The Fieldtype using this Inputfield, or boolean false when known not to have a Fieldtype, or null when not known.
- `$hasField: null|Field` The Field object associated with this Inputfield, or null when not applicable or not known.
- `$hasPage: null|Page` The Page object associated with this Inputfield, or null when not applicable or not known.
- `$hasInputfield: null|Inputfield` If this Inputfield is owned/managed by another (other than parent/child relationship), it may be set here. @since 3.0.176
- `$useLanguages: bool|null` When multi-language support active, can be set to true to make it provide inputs for each language, where supported (default=false).
- `$entityEncodeLabel: null|bool|int` Set to boolean false to specifically disable entity encoding of field header/label (default=true).
- `$entityEncodeText: null|bool` Set to boolean false to specifically disable entity encoding for other text: description, notes, etc. (default=true).
- `$renderFlags: int` Options that can be applied to render, see "render*" constants (default=0). @since 3.0.204
- `$renderValueFlags: int` Options that can be applied to renderValue mode, see "renderValue" constants (default=0).
- [`$wrapClass: string`](method-wrapclass.md) Optional class name (CSS) to apply to the HTML element wrapping the Inputfield.
- [`$headerClass: string`](method-headerclass.md) Optional class name (CSS) to apply to the InputfieldHeader element
- [`$contentClass: string`](method-contentclass.md) Optional class name (CSS) to apply to the InputfieldContent element
- [`$addClass: string`](method-addclass.md) Formatted class string letting you add class to any of the above (see addClass method). @since 3.0.204
- `$textFormat: int|null` Text format to use for description/notes text in Inputfield (see textFormat constants)
- [`required($required = null): string|Inputfield`](method-required.md) Get or set required state. @since 3.0.110
- [`requiredIf($requiredIf = null): string|Inputfield`](method-requiredif.md) Get or set required-if selector. @since 3.0.110
- [`wrapClass($class = null): string|Inputfield`](method-wrapclass.md) Get wrapper class attribute or add a class to it. @since 3.0.110
- [`headerClass($class = null): string|Inputfield`](method-headerclass.md) Get header class attribute or add a class to it. @since 3.0.110
- [`contentClass($class = null): string|Inputfield`](method-contentclass.md) Get content class attribute or add a class to it. @since 3.0.110

## Multi-Language Methods (Requires Languagesupport Module To Be Installed)

- [`setLanguageValue($language, $value): void`](method-setlanguagevalue.md) Set language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238
- [`getLanguageValue($language): string|mixed`](method-getlanguagevalue.md) Get language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238

## Hookable Methods

- [`render(): string`](method-___render.md)
- [`renderValue(): string`](method-___rendervalue.md)
- [`renderReadyHook(Inputfield $parent, $renderValueMode): void`](method-___renderreadyhook.md)
- [`processInput(WireInputData $input): Inputfield`](method-___processinput.md)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md)
- [`getConfigArray(): array`](method-___getconfigarray.md)
- [`getConfigAllowContext(Field $field): array`](method-___getconfigallowcontext.md)

Methods:
- [`__construct()`](method-__construct.md) Construct the Inputfield, setting defaults for all properties
- [`init()`](method-init.md) Per the Module interface, init() is called after any configuration data has been populated to the Inputfield, but before render.
- [`install()`](method-___install.md) (hookable) Per the Module interface, this method is called when this Inputfield is installed
- [`uninstall()`](method-___uninstall.md) (hookable) Per the Module interface, uninstall() is called when this Inputfield is uninstalled
- [`set(string $key, mixed $value): Inputfield|WireData`](method-set.md) Set a property or attribute to the Inputfield
- [`get(string $key): mixed|null`](method-get.md) Get a property or attribute from the Inputfield
- [`getSetting(string $key): mixed`](method-getsetting.md) Gets a setting (or API variable) from the Inputfield, while ignoring attributes.
- [`setParent(InputfieldWrapper $parent): $this`](method-setparent.md) Set the parent (InputfieldWrapper) of this Inputfield.
- [`getParent(): InputfieldWrapper|null`](method-getparent.md) Get this Inputfield’s parent InputfieldWrapper, or NULL if it doesn’t have one.
- [`getParents(): array`](method-getparents.md) Get array of all parents of this Inputfield.
- [`parent(null|InputfieldWrapper $parent = null): null|Inputfield|InputfieldWrapper`](method-parent.md) Get or set parent of Inputfield
- [`parents(): array`](method-parents.md) Get array of all parents of this Inputfield
- [`getRootParent(): InputfieldForm|InputfieldWrapper|null`](method-getrootparent.md) Get the root parent InputfieldWrapper element (farthest parent, commonly InputfieldForm)
- [`getForm(): InputfieldForm|null`](method-getform.md) Get the InputfieldForm element that contains this field or null if not yet defined
- [`removeAttr(string $key): $this`](method-removeattr.md) Remove an attribute
- [`attr(string|array|bool $key, string|int|bool|null $value = null): Inputfield|array|string|int|object|float`](method-attr.md) Get or set an attribute (or multiple attributes)
- [`val(string|null $value = null): string|int|float|array|object|Wire|WireData|WireArray|Inputfield`](method-val.md) Shortcut for getting or setting “value” attribute
- [`wrapAttr(string|null|bool $key = null, string|null|bool $value = null): Inputfield|string|array|null`](method-wrapattr.md) Get or set attribute for the element wrapping this Inputfield
- [`addClass(string|array $class, string $property = 'class'): $this`](method-addclass.md) Add a class or classes to this Inputfield (or a wrapping element)
- [`addClassString(string $class, string $property = 'class'): self`](method-addclassstring.md) Add class(es) by formatted string that lets you specify where class should be added
- [`hasClass(string|array $class, string $property = 'class'): bool`](method-hasclass.md) Does this Inputfield have the given class name (or names)?
- [`getClassArray(string $property = 'class', bool $assoc = false): array`](method-getclassarray.md) Get classes in array for given class property
- [`getClassProperty(string $property): string`](method-getclassproperty.md) Get the internal property name for given class property
- [`removeClass(string|array $class, string $property = 'class'): $this`](method-removeclass.md) Remove the given class (or classes) from this Inputfield
- [`render(): string`](method-___render.md) (hookable) Render the HTML input element(s) markup, ready for insertion in an HTML form.
- [`renderValue(): string`](method-___rendervalue.md) (hookable) Render just the value (not input) in text/markup for presentation purposes.
- [`renderReady(?Inputfield $parent = null, bool $renderValueMode = false): bool`](method-renderready.md) Method called right before Inputfield markup is rendered, so that any dependencies can be loaded as well.
- [`renderReadyHook(?Inputfield $parent = null, bool $renderValueMode = false)`](method-___renderreadyhook.md) (hookable) Hookable version of renderReady(), not called unless 'renderReadyHook' is hooked
- [`processInput(WireInputData $input): $this`](method-___processinput.md) (hookable) Process input for this Inputfield directly from the POST (or GET) variables
- [`isEmpty(): bool`](method-isempty.md) Is this Inputfield empty? (Value attribute reflects an empty state)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable) Get any custom configuration fields for this Inputfield
- [`getConfigArray(): array`](method-___getconfigarray.md) (hookable) Alternative method for configuration that allows for array definition
- [`getConfigAllowContext(Field $field): array`](method-___getconfigallowcontext.md) (hookable) Return a list of config property names allowed for fieldgroup/template context
- [`error(string $text, int $flags = 0): $this`](method-error.md) Record an error for this Inputfield
- [`getErrors(bool $clear = false): array`](method-geterrors.md) Return array of strings containing errors that occurred during input processing
- [`clearErrors()`](method-clearerrors.md) Clear errors from this Inputfield
- [`has(string $key): bool`](method-has.md) Does this Inputfield have the requested property or attribute?
- [`entityEncode(string $str, bool|int $markdown = false): string`](method-entityencode.md) Entity encode a string with optional Markdown support.
- [`editable(bool|null $setEditable = null): bool`](method-editable.md) Get or set editable state for this Inputfield
- [`addHeaderAction(array $settings = array()): array`](method-addheaderaction.md) Add header action
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method

Constants:
- [`collapsedNo = 0`](const-collapsedno.md)
- [`collapsedYes = 1`](const-collapsedyes.md)
- [`collapsedBlank = 2`](const-collapsedblank.md)
- [`collapsedHidden = 4`](const-collapsedhidden.md)
- [`collapsedPopulated = 5`](const-collapsedpopulated.md)
- [`collapsedNoLocked = 6`](const-collapsednolocked.md)
- [`collapsedBlankLocked = 7`](const-collapsedblanklocked.md)
- [`collapsedYesLocked = 8`](const-collapsedyeslocked.md)
- [`collapsedNever = 9`](const-collapsednever.md)
- [`collapsedYesAjax = 10`](const-collapsedyesajax.md)
- [`collapsedBlankAjax = 11`](const-collapsedblankajax.md)
- [`collapsedTab = 20`](const-collapsedtab.md)
- [`collapsedTabAjax = 21`](const-collapsedtabajax.md)
- [`collapsedTabLocked = 22`](const-collapsedtablocked.md)
- [`skipLabelNo = false`](const-skiplabelno.md)
- [`skipLabelFor = true`](const-skiplabelfor.md)
- [`skipLabelHeader = 2`](const-skiplabelheader.md)
- [`skipLabelBlank = 4`](const-skiplabelblank.md)
- [`skipLabelMarkup = 8`](const-skiplabelmarkup.md)
- [`textFormatNone = 2`](const-textformatnone.md)
- [`textFormatBasic = 4`](const-textformatbasic.md)
- [`textFormatMarkdown = 8`](const-textformatmarkdown.md)
- [`renderFirst = 1`](const-renderfirst.md)
- [`renderLast = 2`](const-renderlast.md)
- [`renderValueMinimal = 2`](const-rendervalueminimal.md)
- [`renderValueNoWrap = 4`](const-rendervaluenowrap.md)
- [`renderValueFirst = 8`](const-rendervaluefirst.md)
