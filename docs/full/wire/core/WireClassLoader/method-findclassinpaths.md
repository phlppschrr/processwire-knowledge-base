# $wireClassLoader->findClassInPaths($name, $paths, $dir = ''): string|bool

Source: `wire/core/WireClassLoader.php`

Find class file among given paths and return full pathname to file if found

## Arguments

- string $name Class name without namespace
- string|array $paths Path(s) to check
- string $dir Optional directory string to append to each path, must not start with slash but must end with slash, i.e. "dir/"

## Return value

string|bool Returns full path+filename when found or boolean false when not found

## Meta

- @since 3.0.152
