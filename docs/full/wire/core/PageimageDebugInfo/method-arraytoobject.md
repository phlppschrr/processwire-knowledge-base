# PageimageDebugInfo::arrayToObject()

Source: `wire/core/PageimageDebugInfo.php`

Helper method that converts a multidim array to a multidim object for the getDebugInfo method

@param array $array the input array

@param object $object the initial object, gets passed recursive by reference through all loops

@param bool $multidim set this to true to avoid multidimensional object

@return object the final multidim object
