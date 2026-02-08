# $wireClassLoader->findClassInPaths($name, $paths, $dir = ''): string|bool

Source: `wire/core/WireClassLoader.php`

Find class file among given paths and return full pathname to file if found

## Usage

~~~~~
// basic usage
$string = $wireClassLoader->findClassInPaths($name, $paths);

// usage with all arguments
$string = $wireClassLoader->findClassInPaths($name, $paths, $dir = '');
~~~~~

## Arguments

- `$name` `string` Class name without namespace
- `$paths` `string|array` Path(s) to check
- `$dir` (optional) `string` Optional directory string to append to each path, must not start with slash but must end with slash, i.e. "dir/"

## Return value

- `string|bool` Returns full path+filename when found or boolean false when not found

## Since

3.0.152
