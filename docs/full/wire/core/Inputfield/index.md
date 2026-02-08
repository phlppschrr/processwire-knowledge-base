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

Methods:
Method: [__construct()](method-__construct.md)
Method: [init()](method-init.md)
Method: [___install()](method-___install.md)
Method: [___uninstall()](method-___uninstall.md)
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
Method: [___render()](method-___render.md)
Method: [___renderValue()](method-___rendervalue.md)
Method: [renderReady()](method-renderready.md)
Method: [___renderReadyHook()](method-___renderreadyhook.md)
Method: [___processInput()](method-___processinput.md)
Method: [isEmpty()](method-isempty.md)
Method: [___getConfigInputfields()](method-___getconfiginputfields.md)
Method: [___getConfigArray()](method-___getconfigarray.md)
Method: [___getConfigAllowContext()](method-___getconfigallowcontext.md)
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
