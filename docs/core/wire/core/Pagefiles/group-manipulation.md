# Pagefiles: manipulation

Source: `wire/core/Pagefiles.php`

@method Pagefiles delete() delete(Pagefile $file) Removes the file and deletes from disk when page is saved.

@method Pagefile|bool clone(Pagefile $item, array $options = array()) Duplicate a file and return it.
