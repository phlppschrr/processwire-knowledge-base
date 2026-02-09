# August 2014 Core Updates #1

Source: https://processwire.com/blog/posts/august-2014-core-updates-1/

## Sections


## August 2014 Core Updates #1

4 August 2014 by Ryan Cramer [ 0 Comments](/blog/posts/august-2014-core-updates-1/#comments)


## Field migrations and session namespaces


### Field export/import capability

[](//d1juguve2xwkcy.cloudfront.net/assets/files/6304/post-2-0-55520000-1406842384.png)This feature is to answer the question of how to migrate field changes more easily. With this new feature, migrating field changes or additions is as easy as copying and pasting some text (literally!) – here's how it works:

- In your admin, if you browse to Setup > Fields, you'll see two new buttons in the bottom right corner: Export and Import. Click the Export button and you'll get a screen that lets you select one or more (or all) fields in your site for export to another ProcessWire installation. This exports all the settings of selected fields to JSON format and puts it in your copy/paste queue.
- Go to another ProcessWire installation and click to Setup > Fields > Import. Paste in the data you just exported, click Preview, and it'll show you what's different from your current configuration. Following that, it'll give you the option of committing any of the changes/additions that you choose.

Behind the scenes, when creating an export, ProcessWire converts internal references for resources like pages and templates to external references to make them cross-site portable. To put that another way, the IDs of resources don't have to match up between the two sites. This opens up the ability to migrate fields between completely different sites.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/6304/post-2-0-79528500-1406842393.png)Importing doesn't have to be an all-or-nothing operation. When performing a field export/import, there is always a chance that some expected resource or module isn't available on the importing site. But this is not a fatal error to the import tool. Instead, it will let you continue to import the fields (and properties of those fields) that you decide. This gives you the ability to complete any remaining configuration on your own.

Like everything in ProcessWire, it's also API accessible. If you are interested in that side of it, see the new Exportable interface, which lets you assume any classes implementing it to have`getExportData()` and `setImportData(array $data)` methods:

- `$item->getExportData()` takes no arguments and returns an array of portable data ready for import somewhere else.
- `$item->setImportData($data)` accepts `$data` array as it's only argument and populates the `$item` with that data. It returns an array indexed by property name of everything that changed, along with the old value, new value and any error messages or warnings that accompanied it.

If you want to commit the changes, all you need to do is `$item->save()`.

The field export/import is actually just the first in a series of upcoming updates enabling more simple migration of configuration data in ProcessWire. Coming next will be the same exact tool, but for migrating templates (including related field assignments/fieldgroups).

There has been interest among some in keeping field and template changes under version control, so we will also be providing a module that mirrors every change to a field/template to JSON files (which will also be supported by the import tools).


### $session namespaces

When you use `$session->set('foo', 'bar')` you are setting the property named "foo" within the same namespace as anything else that might be using `$session` to remember values. If another process happens to set its own value for "foo", you've got a name collision.

Admittedly, name collisions aren't likely just because most people setting session variables are making them a whole lot more specific than "foo". But the truth is you really shouldn't have to think about stuff like that.

This week we've added session namespace support so that you can optionally specify a namespace that your value should live within. This ensures that you won't have the potential for name collisions in session variables. Here's how you use it:

```
$session->set($this, 'foo', 'bar');
$bar = $session->get($this, 'foo');
```

When given an object instance (like `$this`) or your own namespace (string), the values you set are only accessible within that namespace. If you later call `$session->get('foo')`, you won't get the value you set before, because your namespace wasn't specified. Of course, the non-namespace syntax works as it always has, so this is all backwards compatible.
