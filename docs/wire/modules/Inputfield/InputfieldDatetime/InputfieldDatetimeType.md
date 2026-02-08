# InputfieldDatetimeType

Source: `wire/modules/Inputfield/InputfieldDatetime/InputfieldDatetimeType.php`


## __construct()

Construct

@param InputfieldDatetime $inputfield

## getTypeName()

Get name for this type

@return string

## getTypeLabel()

Get type label

@return string

## getAttribute()

Get attribute

@param string $key

@return string|null

## setAttribute()

Get attribute

@param string $key

@param string $value

@return self

## getSetting()

Get setting

@param string $key

@return mixed

## get()

Get setting or attribute or API var

@param string $key

@return mixed|null

## getDefaultSettings()

Get array of default settings

@return array

## renderValue()

@return string

## sanitizeValue()

Sanitize value to unix timestamp integer or blank string (to represent no value)

@param string|int $value

@return int|string

## renderReady()

Render ready

## render()

@return string

## processInput()

Process input

@param WireInputData $input

@return int|string|bool Int for UNIX timestamp date, blank string for no date, or boolean false if InputfieldDatetime should process input

## getConfigInputfields()

@param InputfieldWrapper $inputfields
