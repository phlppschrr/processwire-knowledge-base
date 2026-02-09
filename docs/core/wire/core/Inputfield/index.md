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

ATTRIBUTES
==========

- [`$name: string`](method-name.md) HTML 'name' attribute for Inputfield (required).
- [`$id: string`](method-id.md) HTML 'id' attribute for the Inputfield (if not yet, determined automatically).
- `$value: mixed` HTML 'value' attribute for the Inputfield.
- [`$class: string`](method-class.md) HTML 'class' attribute for the Inputfield.
- [`name($name = null): string|Inputfield`](method-name.md) Get or set the name attribute. @since 3.0.110
- [`id($id = null): string|Inputfield`](method-id.md) Get or set the id attribute. @since 3.0.110
- [`class($class = null): string|Inputfield`](method-class.md) Get class attribute or add a class to the class attribute. @since 3.0.110

LABELS & CONTENT
================

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

APPEARANCE
==========

- [`$collapsed: int`](method-collapsed.md) Whether the field is collapsed or visible, using one of the "collapsed" constants.
- [`$showIf: string`](method-showif.md) Optional conditions under which the Inputfield appears in the form (selector string).
- [`$columnWidth: int`](method-columnwidth.md) Width of column for this Inputfield 10-100 percent. 0 is assumed to be 100 (default).
- [`$skipLabel: int`](method-skiplabel.md) Skip display of the label? See the "skipLabel" constants for options.
- [`collapsed($collapsed = null): int|Inputfield`](method-collapsed.md) Get or set collapsed property via method. @since 3.0.110
- [`showIf($showIf = null): string|Inputfield`](method-showif.md) Get or set showIf selector property via method. @since 3.0.110
- [`columnWidth($columnWidth = null): int|Inputfield`](method-columnwidth.md) Get or set columnWidth property via method. @since 3.0.110
- [`skipLabel($skipLabel = null): int|Inputfield`](method-skiplabel.md) Get or set the skipLabel constant property via method. @since 3.0.110

UIKIT THEME
===========

- `$themeOffset: bool|string` Offset/margin for Inputfield, one of 's', 'm', or 'l'.
- `$themeBorder: string` Border style for Inputfield, one of 'none', 'card', 'hide' or 'line'.
- `$themeInputSize: string` Input size height/font within Inputfield, one of 's', 'm', or 'l'.
- `$themeInputWidth: string` Input width for text-type inputs, one of 'xs', 's', 'm', 'l', or 'f' (for full-width).
- `$themeColor: string` Color theme for Inputfield, one of 'primary', 'secondary', 'warning', 'danger', 'success', 'highlight', 'none'.
- `$themeBlank: bool` Makes <input> element display with no minimal container / no border when true.

SETTINGS & BEHAVIOR
===================

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

MULTI-LANGUAGE METHODS (requires LanguageSupport module to be installed)
======================

- [`setLanguageValue($language, $value): void`](method-setlanguagevalue.md) Set language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238
- [`getLanguageValue($language): string|mixed`](method-getlanguagevalue.md) Get language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238

Methods:
- [`__construct()`](method-__construct.md)
- [`init()`](method-init.md)
- [`install()`](method-___install.md) (hookable)
- [`uninstall()`](method-___uninstall.md) (hookable)
- [`set(string $key, mixed $value): Inputfield|WireData`](method-set.md)
- [`get(string $key): mixed|null`](method-get.md)
- [`getSetting(string $key): mixed`](method-getsetting.md)
- [`setParent(InputfieldWrapper $parent): $this`](method-setparent.md)
- [`getParent(): InputfieldWrapper|null`](method-getparent.md)
- [`getParents(): array`](method-getparents.md)
- [`parent(null|InputfieldWrapper $parent = null): null|Inputfield|InputfieldWrapper`](method-parent.md)
- [`parents(): array`](method-parents.md)
- [`getRootParent(): InputfieldForm|InputfieldWrapper|null`](method-getrootparent.md)
- [`getForm(): InputfieldForm|null`](method-getform.md)
- [`removeAttr(string $key): $this`](method-removeattr.md)
- [`attr(string|array|bool $key, string|int|bool|null $value = null): Inputfield|array|string|int|object|float`](method-attr.md)
- [`val(string|null $value = null): string|int|float|array|object|Wire|WireData|WireArray|Inputfield`](method-val.md)
- [`wrapAttr(string|null|bool $key = null, string|null|bool $value = null): Inputfield|string|array|null`](method-wrapattr.md)
- [`addClass(string|array $class, string $property = 'class'): $this`](method-addclass.md)
- [`addClassString(string $class, string $property = 'class'): self`](method-addclassstring.md)
- [`hasClass(string|array $class, string $property = 'class'): bool`](method-hasclass.md)
- [`getClassArray(string $property = 'class', bool $assoc = false): array`](method-getclassarray.md)
- [`getClassProperty(string $property): string`](method-getclassproperty.md)
- [`removeClass(string|array $class, string $property = 'class'): $this`](method-removeclass.md)
- [`render(): string`](method-___render.md) (hookable)
- [`renderValue(): string`](method-___rendervalue.md) (hookable)
- [`renderReady(?Inputfield $parent = null, bool $renderValueMode = false): bool`](method-renderready.md)
- [`renderReadyHook(?Inputfield $parent = null, bool $renderValueMode = false)`](method-___renderreadyhook.md) (hookable)
- [`processInput(WireInputData $input): $this`](method-___processinput.md) (hookable)
- [`isEmpty(): bool`](method-isempty.md)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable)
- [`getConfigArray(): array`](method-___getconfigarray.md) (hookable)
- [`getConfigAllowContext(Field $field): array`](method-___getconfigallowcontext.md) (hookable)
- [`error(string $text, int $flags = 0): $this`](method-error.md)
- [`getErrors(bool $clear = false): array`](method-geterrors.md)
- [`clearErrors()`](method-clearerrors.md)
- [`has(string $key): bool`](method-has.md)
- [`entityEncode(string $str, bool|int $markdown = false): string`](method-entityencode.md)
- [`editable(bool|null $setEditable = null): bool`](method-editable.md)
- [`addHeaderAction(array $settings = array()): array`](method-addheaderaction.md)
- [`__debugInfo(): array`](method-__debuginfo.md)

Constants:
- [`collapsedNo`](const-collapsedno.md)
- [`collapsedYes`](const-collapsedyes.md)
- [`collapsedBlank`](const-collapsedblank.md)
- [`collapsedHidden`](const-collapsedhidden.md)
- [`collapsedPopulated`](const-collapsedpopulated.md)
- [`collapsedNoLocked`](const-collapsednolocked.md)
- [`collapsedBlankLocked`](const-collapsedblanklocked.md)
- [`collapsedYesLocked`](const-collapsedyeslocked.md)
- [`collapsedNever`](const-collapsednever.md)
- [`collapsedYesAjax`](const-collapsedyesajax.md)
- [`collapsedBlankAjax`](const-collapsedblankajax.md)
- [`collapsedTab`](const-collapsedtab.md)
- [`collapsedTabAjax`](const-collapsedtabajax.md)
- [`collapsedTabLocked`](const-collapsedtablocked.md)
- [`skipLabelNo`](const-skiplabelno.md)
- [`skipLabelFor`](const-skiplabelfor.md)
- [`skipLabelHeader`](const-skiplabelheader.md)
- [`skipLabelBlank`](const-skiplabelblank.md)
- [`skipLabelMarkup`](const-skiplabelmarkup.md)
- [`textFormatNone`](const-textformatnone.md)
- [`textFormatBasic`](const-textformatbasic.md)
- [`textFormatMarkdown`](const-textformatmarkdown.md)
- [`renderFirst`](const-renderfirst.md)
- [`renderLast`](const-renderlast.md)
- [`renderValueMinimal`](const-rendervalueminimal.md)
- [`renderValueNoWrap`](const-rendervaluenowrap.md)
- [`renderValueFirst`](const-rendervaluefirst.md)

HOOKABLE METHODS
================

- [`render(): string`](method-___render.md)
- [`renderValue(): string`](method-___rendervalue.md)
- [`renderReadyHook(Inputfield $parent, $renderValueMode): void`](method-___renderreadyhook.md)
- [`processInput(WireInputData $input): Inputfield`](method-___processinput.md)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md)
- [`getConfigArray(): array`](method-___getconfigarray.md)
- [`getConfigAllowContext(Field $field): array`](method-___getconfigallowcontext.md)
