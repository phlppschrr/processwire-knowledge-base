# Pageimage::webp()

Source: `wire/core/Pageimage.php`

Get WebP "extra" version of this Pageimage

@param array $webpOptions Optionally override certain defaults from `$config->webpOptions` (requires 3.0.229+):
 - `useSrcUrlOnSize` (bool): Fallback to source file URL when webp file is larger than source? (default=true)
 - `useSrcUrlOnFail` (bool): Fallback to source file URL when webp file fails for some reason? (default=true)
 - `quality' (int): Quality setting of 1-100 where higher is better but larger in file size (default=90)
    Note that his quality setting is only used if the .webp file does not already exist.

@return PagefileExtra

@since 3.0.132
