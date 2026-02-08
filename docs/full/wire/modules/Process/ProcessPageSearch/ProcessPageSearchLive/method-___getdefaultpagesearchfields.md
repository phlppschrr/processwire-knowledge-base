# ProcessPageSearchLive::___getDefaultPageSearchFields()

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Get the names of fields that should be used when searching pages

Hook this from /site/templates/admin.php to modify what gets searched.
This overrides the setting specified interactively in the ProcessPageSearch module settings.

~~~~~
$wire->addHookAfter('ProcessPageSearchLive::getDefaultPageSearchFields', function(HookEvent $e) {
  $e->return = [ 'title', 'subtitle', 'categories.title' ];
});
~~~~~


@return array

@since 3.0.242
