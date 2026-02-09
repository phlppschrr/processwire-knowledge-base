# CommentForm

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentForm.php`

Inherits: `Wire`
Implements: `CommentFormInterface`

## Summary

Default/example implementation of the CommentFormInterface

Common methods:
- [`setOptions()`](method-setoptions.md)
- [`getOptions()`](method-getoptions.md)
- [`arrayOption()`](method-arrayoption.md)
- [`labels()`](method-labels.md)
- [`attrs()`](method-attrs.md)

Generates a user input form for comments, processes comment input, and saves to the page

@see CommentArray::renderForm()

## Methods
- [`__construct(Page $page, CommentArray $comments, array $options = array())`](method-__construct.md) Construct a CommentForm
- [`setOptions(array $options)`](method-setoptions.md) Initialize and set options
- [`getOptions(): array`](method-getoptions.md) Get options
- [`arrayOption(string $property, string|array $name = '', string|null $value = null): string|array`](method-arrayoption.md) Get or set array property
- [`labels(string $name, string|null $value = null): string`](method-labels.md) Get or set label
- [`attrs(string $name, string|null $value = null): string`](method-attrs.md) Get or set attribute
- [`classes(string $name, string|null $value = null): string`](method-classes.md) Get or set class(es)
- [`markup(string $name, string|null $value = null): string`](method-markup.md) Get or set markup
- [`presets(string $name, string|null $value = null): string`](method-presets.md) Get or set presets
- [`setAttr(string $attr, string $value)`](method-setattr.md) Set attribute
- [`setLabel(string $label, string $value)`](method-setlabel.md) Set label
- [`renderSuccess(?Comment $comment = null): string`](method-rendersuccess.md) Replaces the output of the render() method when a Comment is posted
- [`render(): string`](method-render.md) Render the CommentForm output and process the input if it's been submitted
- [`renderForm(string $id, string $class, array $attrs, array $labels, array $inputValues): string`](method-renderform.md) Render form
- [`renderFormNormal(string $id, string $class, array $attrs, array $labels, array $inputValues): string`](method-renderformnormal.md) Render normal form without threaded comments possibility
- [`renderFormThread(string $id, string $class, array $attrs, array $labels, array $inputValues): string`](method-renderformthread.md) Render form for threaded (depth) comments
- [`renderNotifyOptions(): string`](method-rendernotifyoptions.md) Render the "notify me" options
- [`processInput(): Comment|bool`](method-processinput.md) Process a submitted CommentForm, insert the Comment, and save the Page
- [`getPostedComment()`](method-getpostedcomment.md) Return the Comment that was posted or NULL if not yet posted
