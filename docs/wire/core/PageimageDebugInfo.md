# PageimageDebugInfo

Source: `wire/core/PageimageDebugInfo.php`

Debug info for Pageimage

By Horst Nogajski for ProcessWire

## other

@property string $url

@property string $filename

@property string $basename

@property Pageimage $original

@property int $width

@property int $height

@property bool $hasFocus

@property string $focusStr

@property string $suffixStr

## __construct()

Construct

@param Pageimage $pageimage

## get()

Get property

This primarily delegates to the Pageimage object so that its properties can be accessed
directly from this class.

@param string $key

@return mixed|null

## getBasicDebugInfo()

Get basic debug info, like that used for Pageimage::__debugInfo()

@return array

## getVerboseDebugInfo()

Get verbose DebugInfo, optionally with individual options array, @horst

(without invoking the magic debug)

@param array $options The individual options you also passes with your image variation creation

@param string $returnType 'string'|'array'|'object', default is 'string' and returns markup or plain text

@return array|object|string

## arrayToObject()

Helper method that converts a multidim array to a multidim object for the getDebugInfo method

@param array $array the input array

@param object $object the initial object, gets passed recursive by reference through all loops

@param bool $multidim set this to true to avoid multidimensional object

@return object the final multidim object
