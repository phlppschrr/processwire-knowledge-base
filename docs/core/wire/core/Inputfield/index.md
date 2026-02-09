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

- [$name: string](method-name.md) HTML 'name' attribute for Inputfield (required).
- [$id: string](method-id.md) HTML 'id' attribute for the Inputfield (if not yet, determined automatically).
- $value: mixed HTML 'value' attribute for the Inputfield.
- [$class: string](method-class.md) HTML 'class' attribute for the Inputfield.
- [name($name = null): string|Inputfield](method-name.md) Get or set the name attribute. @since 3.0.110
- [id($id = null): string|Inputfield](method-id.md) Get or set the id attribute. @since 3.0.110
- [class($class = null): string|Inputfield](method-class.md) Get class attribute or add a class to the class attribute. @since 3.0.110

LABELS & CONTENT
================

- [$label: string](method-label.md) Primary label text that appears above the input.
- [$description: string](method-description.md) Optional description that appears under label to provide more detailed information.
- [$notes: string](method-notes.md) Optional notes that appear under input area to provide additional notes.
- $detail: string Optional text details that appear under notes. @since 3.0.140
- [$icon: string](method-icon.md) Optional font-awesome icon name to accompany label (excluding the "fa-") part).
- [$requiredLabel: string](method-requiredlabel.md) Optional custom label to display when missing required value. @since 3.0.98
- $tabLabel: string Label for tab if Inputfield rendered in its own tab via Inputfield::collapsedTab* setting. @since 3.0.201
- [$prependMarkup: string|null](method-prependmarkup.md) Optional markup to prepend to the Inputfield content container.
- [$appendMarkup: string|null](method-appendmarkup.md) Optional markup to append to the Inputfield content container.
- $footerMarkup: string|null Optional markup to add to the '.Inputfield' container, after '.InputfieldContent'. @since 3.0.241
- [label($label = null): string|Inputfield](method-label.md) Get or set the 'label' property via method. @since 3.0.110
- [description($description = null): string|Inputfield](method-description.md) Get or set the 'description' property via method. @since 3.0.110
- [notes($notes = null): string|Inputfield](method-notes.md) Get or set the 'notes' property via method. @since 3.0.110
- [icon($icon = null): string|Inputfield](method-icon.md) Get or set the 'icon' property via method. @since 3.0.110
- [requiredLabel($requiredLabel = null): string|Inputfield](method-requiredlabel.md) Get or set the 'requiredLabel' property via method. @since 3.0.110
- [head($head = null): string|Inputfield](method-head.md) Get or set the 'head' property via method. @since 3.0.110
- [prependMarkup($markup = null): string|Inputfield](method-prependmarkup.md) Get or set the 'prependMarkup' property via method. @since 3.0.110
- [appendMarkup($markup = null): string|Inputfield](method-appendmarkup.md) Get or set the 'appendMarkup' property via method. @since 3.0.110

APPEARANCE
==========

- [$collapsed: int](method-collapsed.md) Whether the field is collapsed or visible, using one of the "collapsed" constants.
- [$showIf: string](method-showif.md) Optional conditions under which the Inputfield appears in the form (selector string).
- [$columnWidth: int](method-columnwidth.md) Width of column for this Inputfield 10-100 percent. 0 is assumed to be 100 (default).
- [$skipLabel: int](method-skiplabel.md) Skip display of the label? See the "skipLabel" constants for options.
- [collapsed($collapsed = null): int|Inputfield](method-collapsed.md) Get or set collapsed property via method. @since 3.0.110
- [showIf($showIf = null): string|Inputfield](method-showif.md) Get or set showIf selector property via method. @since 3.0.110
- [columnWidth($columnWidth = null): int|Inputfield](method-columnwidth.md) Get or set columnWidth property via method. @since 3.0.110
- [skipLabel($skipLabel = null): int|Inputfield](method-skiplabel.md) Get or set the skipLabel constant property via method. @since 3.0.110

UIKIT THEME
===========

- $themeOffset: bool|string Offset/margin for Inputfield, one of 's', 'm', or 'l'.
- $themeBorder: string Border style for Inputfield, one of 'none', 'card', 'hide' or 'line'.
- $themeInputSize: string Input size height/font within Inputfield, one of 's', 'm', or 'l'.
- $themeInputWidth: string Input width for text-type inputs, one of 'xs', 's', 'm', 'l', or 'f' (for full-width).
- $themeColor: string Color theme for Inputfield, one of 'primary', 'secondary', 'warning', 'danger', 'success', 'highlight', 'none'.
- $themeBlank: bool Makes <input> element display with no minimal container / no border when true.

SETTINGS & BEHAVIOR
===================

- [$required: int|bool](method-required.md) Set to true (or 1) to make input required, or false (or 0) to make not required (default=0).
- [$requiredIf: string](method-requiredif.md) Optional conditions under which input is required (selector string).
- $requiredAttr: int|bool|null Use HTML5 “required” attribute when used by Inputfield and $required is true? Default=null.
- $hasFieldtype: null|bool|Fieldtype The Fieldtype using this Inputfield, or boolean false when known not to have a Fieldtype, or null when not known.
- $hasField: null|Field The Field object associated with this Inputfield, or null when not applicable or not known.
- $hasPage: null|Page The Page object associated with this Inputfield, or null when not applicable or not known.
- $hasInputfield: null|Inputfield If this Inputfield is owned/managed by another (other than parent/child relationship), it may be set here. @since 3.0.176
- $useLanguages: bool|null When multi-language support active, can be set to true to make it provide inputs for each language, where supported (default=false).
- $entityEncodeLabel: null|bool|int Set to boolean false to specifically disable entity encoding of field header/label (default=true).
- $entityEncodeText: null|bool Set to boolean false to specifically disable entity encoding for other text: description, notes, etc. (default=true).
- $renderFlags: int Options that can be applied to render, see "render*" constants (default=0). @since 3.0.204
- $renderValueFlags: int Options that can be applied to renderValue mode, see "renderValue" constants (default=0).
- [$wrapClass: string](method-wrapclass.md) Optional class name (CSS) to apply to the HTML element wrapping the Inputfield.
- [$headerClass: string](method-headerclass.md) Optional class name (CSS) to apply to the InputfieldHeader element
- [$contentClass: string](method-contentclass.md) Optional class name (CSS) to apply to the InputfieldContent element
- [$addClass: string](method-addclass.md) Formatted class string letting you add class to any of the above (see addClass method). @since 3.0.204
- $textFormat: int|null Text format to use for description/notes text in Inputfield (see textFormat constants)
- [required($required = null): string|Inputfield](method-required.md) Get or set required state. @since 3.0.110
- [requiredIf($requiredIf = null): string|Inputfield](method-requiredif.md) Get or set required-if selector. @since 3.0.110
- [wrapClass($class = null): string|Inputfield](method-wrapclass.md) Get wrapper class attribute or add a class to it. @since 3.0.110
- [headerClass($class = null): string|Inputfield](method-headerclass.md) Get header class attribute or add a class to it. @since 3.0.110
- [contentClass($class = null): string|Inputfield](method-contentclass.md) Get content class attribute or add a class to it. @since 3.0.110

MULTI-LANGUAGE METHODS (requires LanguageSupport module to be installed)
======================

- [setLanguageValue($language, $value): void](method-setlanguagevalue.md) Set language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238
- [getLanguageValue($language): string|mixed](method-getlanguagevalue.md) Get language value for Inputfield that supports it. Requires LanguageSupport module. $language can be Language, id (int) or name (string). @since 3.0.238

Methods:
Method: [__construct()](method-__construct.md)
Method: [init()](method-init.md)
Method: [install()](method-___install.md) (hookable)
Method: [uninstall()](method-___uninstall.md) (hookable)
Method: [set()](method-set.md)
Method: [get()](method-get.md)
Method: [getSetting()](method-getsetting.md)
Method: [setParent()](method-setparent.md)
Method: [getParent()](method-getparent.md)
Method: [getParents()](method-getparents.md)
Method: [parent()](method-parent.md)
Method: [parents()](method-parents.md)
Method: [getRootParent()](method-getrootparent.md)
Method: [getForm()](method-getform.md)
Method: [removeAttr()](method-removeattr.md)
Method: [attr()](method-attr.md)
Method: [val()](method-val.md)
Method: [wrapAttr()](method-wrapattr.md)
Method: [addClass()](method-addclass.md)
Method: [addClassString()](method-addclassstring.md)
Method: [hasClass()](method-hasclass.md)
Method: [getClassArray()](method-getclassarray.md)
Method: [getClassProperty()](method-getclassproperty.md)
Method: [removeClass()](method-removeclass.md)
Method: [render()](method-___render.md) (hookable)
Method: [renderValue()](method-___rendervalue.md) (hookable)
Method: [renderReady()](method-renderready.md)
Method: [renderReadyHook()](method-___renderreadyhook.md) (hookable)
Method: [processInput()](method-___processinput.md) (hookable)
Method: [isEmpty()](method-isempty.md)
Method: [getConfigInputfields()](method-___getconfiginputfields.md) (hookable)
Method: [getConfigArray()](method-___getconfigarray.md) (hookable)
Method: [getConfigAllowContext()](method-___getconfigallowcontext.md) (hookable)
Method: [error()](method-error.md)
Method: [getErrors()](method-geterrors.md)
Method: [clearErrors()](method-clearerrors.md)
Method: [has()](method-has.md)
Method: [entityEncode()](method-entityencode.md)
Method: [editable()](method-editable.md)
Method: [addHeaderAction()](method-addheaderaction.md)
Method: [__debugInfo()](method-__debuginfo.md)

Constants:
Const: [collapsedNo](const-collapsedno.md)
Const: [collapsedYes](const-collapsedyes.md)
Const: [collapsedBlank](const-collapsedblank.md)
Const: [collapsedHidden](const-collapsedhidden.md)
Const: [collapsedPopulated](const-collapsedpopulated.md)
Const: [collapsedNoLocked](const-collapsednolocked.md)
Const: [collapsedBlankLocked](const-collapsedblanklocked.md)
Const: [collapsedYesLocked](const-collapsedyeslocked.md)
Const: [collapsedNever](const-collapsednever.md)
Const: [collapsedYesAjax](const-collapsedyesajax.md)
Const: [collapsedBlankAjax](const-collapsedblankajax.md)
Const: [collapsedTab](const-collapsedtab.md)
Const: [collapsedTabAjax](const-collapsedtabajax.md)
Const: [collapsedTabLocked](const-collapsedtablocked.md)
Const: [skipLabelNo](const-skiplabelno.md)
Const: [skipLabelFor](const-skiplabelfor.md)
Const: [skipLabelHeader](const-skiplabelheader.md)
Const: [skipLabelBlank](const-skiplabelblank.md)
Const: [skipLabelMarkup](const-skiplabelmarkup.md)
Const: [textFormatNone](const-textformatnone.md)
Const: [textFormatBasic](const-textformatbasic.md)
Const: [textFormatMarkdown](const-textformatmarkdown.md)
Const: [renderFirst](const-renderfirst.md)
Const: [renderLast](const-renderlast.md)
Const: [renderValueMinimal](const-rendervalueminimal.md)
Const: [renderValueNoWrap](const-rendervaluenowrap.md)
Const: [renderValueFirst](const-rendervaluefirst.md)

HOOKABLE METHODS
================

- [render(): string](method-___render.md)
- [renderValue(): string](method-___rendervalue.md)
- [renderReadyHook(Inputfield $parent, $renderValueMode): void](method-___renderreadyhook.md)
- [processInput(WireInputData $input): Inputfield](method-___processinput.md)
- [getConfigInputfields(): InputfieldWrapper](method-___getconfiginputfields.md)
- [getConfigArray(): array](method-___getconfigarray.md)
- [getConfigAllowContext(Field $field): array](method-___getconfigallowcontext.md)
