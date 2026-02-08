# WireClassLoader::findClassInPaths()

Source: `wire/core/WireClassLoader.php`

Find class file among given paths and return full pathname to file if found

@param string $name Class name without namespace

@param string|array $paths Path(s) to check

@param string $dir Optional directory string to append to each path, must not start with slash but must end with slash, i.e. "dir/"

@return string|bool Returns full path+filename when found or boolean false when not found

@since 3.0.152
