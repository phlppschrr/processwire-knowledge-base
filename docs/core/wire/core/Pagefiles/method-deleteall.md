# Pagefiles::deleteAll()

Source: `wire/core/Pagefiles.php`

Delete all files associated with this Pagefiles instance, leaving a blank Pagefiles instance.

The actual deletion of the files does not take effect until `$page->save()`.


@return $this
