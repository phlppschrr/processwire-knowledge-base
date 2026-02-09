# PageimageDebugInfo

Source: `wire/core/PageimageDebugInfo.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

Debug info for Pageimage

By Horst Nogajski for ProcessWire

Methods:
- [`__construct(Pageimage $pageimage)`](method-__construct.md) Construct
- [`get(string $key): mixed|null`](method-get.md) Get property
- [`getBasicDebugInfo(): array`](method-getbasicdebuginfo.md) Get basic debug info, like that used for Pageimage::__debugInfo()
- [`getVerboseDebugInfo(array $options = array(), string $returnType = 'string'): array|object|string`](method-getverbosedebuginfo.md) Get verbose DebugInfo, optionally with individual options array, @horst
- [`arrayToObject(array $array, object &$object, bool $multidim = true): object`](method-arraytoobject.md) Helper method that converts a multidim array to a multidim object for the getDebugInfo method
