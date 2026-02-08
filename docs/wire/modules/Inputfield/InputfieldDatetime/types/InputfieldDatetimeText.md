# InputfieldDatetimeText

Source: `wire/modules/Inputfield/InputfieldDatetime/types/InputfieldDatetimeText.php`

Text date input types with optional jQuery UI datepicker

## datepickerNo

jQuery UI datepicker: None

## datepickerClick

jQuery UI datepicker: Click button to show

## datepickerInline

jQuery UI datepicker: Inline datepicker always visible (no timepicker support)

## datepickerFocus

jQuery UI datepicker: Show when input focused (recommend option when using datepicker)

## getDefaultSettings()

@return array

## renderReady()

Render ready

## render()

@return string

## renderValue()

Render value

@return string

## processInput()

@param WireInputData $input

@return int|string|bool

## getInputFormat()

Get the input format string for the user's language

@param bool $getArray

@return string|array of dateInputFormat timeInputFormat

## sanitizeValue()

Sanitize value

@param int|string $value

@return int|string

## getConfigInputfields()

@param InputfieldWrapper $inputfields
