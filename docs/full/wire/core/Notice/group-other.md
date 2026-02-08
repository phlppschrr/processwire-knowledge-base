# Notice: other

Source: `wire/core/Notice.php`

@property string|object|array $text Text or value of notice

@property string $class Class of notice

@property int $timestamp Unix timestamp of when the notice was generated

@property int $flags Bitmask using any of the Notice::constants

@property-read $flagsArray Current flags as an array where indexes are int flags and values are flag names (since 3.0.149)

@property-read $flagsStr Current flags as string of flag names (since 3.0.149)

@property string $icon Name of icon to use with Notice

@property string $idStr Unique ID string for Notice

@property int $qty Number of times this Notice was added.
