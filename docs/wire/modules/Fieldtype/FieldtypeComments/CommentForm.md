# CommentForm

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentForm.php`

Default/example implementation of the CommentFormInterface

Generates a user input form for comments, processes comment input, and saves to the page

@see CommentArray::renderForm()

## __construct()

Construct a CommentForm

@param Page $page The page with the comments

@param CommentArray $comments The field value from $page

@param array $options Optional modifications to default behavior (see CommentForm::$options)

## setOptions()

Initialize and set options

@param array $options

## getOptions()

Get options

@return array

## arrayOption()

Get or set array property

@param string $property Name of array property: labels, markup, classes, attrs, presets

@param string|array $name Name of item to get or set or omit to get all, or assoc array to set all/multiple (and omit $value)

@param string|null $value Value to set (if setting) or omit if getting

@return string|array

@throws WireException

@since 3.0.153

## labels()

Get or set label

@param string $name

@param string|null $value

@return string

@since 3.0.153

## attrs()

Get or set attribute

@param string $name

@param string|null $value

@return string

@since 3.0.153

## classes()

Get or set class(es)

@param string $name

@param string|null $value

@return string

@since 3.0.153

## markup()

Get or set markup

@param string $name

@param string|null $value

@return string

@since 3.0.153

## presets()

Get or set presets

@param string $name

@param string|null $value

@return string

@since 3.0.153

## setAttr()

Set attribute

@param string $attr

@param string $value

@deprecated Use attrs() method instead

## setLabel()

Set label

@param string $label Label name

@param string $value Label value

@deprecated Use labels() method instead

## renderSuccess()

Replaces the output of the render() method when a Comment is posted

A success message is shown rather than the form.

@param Comment|null $comment

@return string

## render()

Render the CommentForm output and process the input if it's been submitted

@return string

## renderForm()

Render form

@param string $id

@param string $class

@param array $attrs

@param array $labels

@param array $inputValues

@return string

## renderFormNormal()

Render normal form without threaded comments possibility

@param string $id

@param string $class

@param array $attrs

@param array $labels

@param array $inputValues

@return string

## renderFormThread()

Render form for threaded (depth) comments

@param string $id

@param string $class

@param array $attrs

@param array $labels

@param array $inputValues

@return string

## renderNotifyOptions()

Render the "notify me" options

@return string

## processInput()

Process a submitted CommentForm, insert the Comment, and save the Page

@return Comment|bool

## getPostedComment()

Return the Comment that was posted or NULL if not yet posted
