# InputfieldWrapper::___renderInputfield()

Source: `wire/core/InputfieldWrapper.php`

Render output for an individual Inputfield

This method takes care of all the pre-and-post requisites needed for rendering an Inputfield
among a group of Inputfields. It is used by the `InputfieldWrapper::render()` method for each
Inputfield present in the children.


@param Inputfield $inputfield The Inputfield to render.

@param bool $renderValueMode Specify true if we are only rendering values (default=false).

@return string Rendered output
