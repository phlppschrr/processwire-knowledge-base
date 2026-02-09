# August 2014 Core Updates #3

Source: https://processwire.com/blog/posts/august-2014-core-updates-3/

## Sections


## August 2014 Core Updates #3

19 August 2014 by Ryan Cramer [ 0 Comments](/blog/posts/august-2014-core-updates-3/#comments)


### ProcessWire 2.5 testing

We are adjusting our focus to preparing ProcessWire 2.5 for release, so the pace of our core additions will slow a bit over the next couple of weeks. We are already starting to lock down the feature set and work to refine what's already there to make it fully stable for the upcoming 2.5 release.

We appreciate your help testing. In particular, we'd like to know how it works for you when upgrading existing 2.3 or 2.4 installations. As this is still a development version, it's preferable to test on non-production sites or those where you won't be devastated if something goes wrong. That being said, we're using the latest development version on ProcessWire.com, among other sites, and it's been smooth sailing so far.

If you want to grab a copy of the dev branch to test, please visit GitHub (and make sure your selected branch is "dev"): [https://github.com/ryancramerdesign/ProcessWire/tree/dev](https://github.com/ryancramerdesign/ProcessWire/tree/dev).


### Template export/import

A couple of weeks ago, we showed you the new Field export/import functions. Now we've got the same thing available for Templates. Migrating templates and field definitions (including contexts) is now as simple as copy and paste. Here's how it works:

- In your admin, go to Setup > Templates. In the lower right corner, notice the new Exportand Import buttons. Click the Export button.
- Select one or more templates to export and click Export.
- On another site, go to Setup > Templates > and click Import this time. Paste in the data that was generated from your export.
- The next screen tells you what it found and gives you the opportunity to decide what gets created, modified or removed. Review the details and when ready, click Commit Changes.

As you might expect, this tool can modify existing templates and fieldgroups, or create new ones. If you are also migrating fields, you'll want to use the nearly identical Field export/import tool first (in Setup > Fields), so that your template import has all the fields it needs to re-create your templates/fieldgroups in full.

One other thing to note is that this tool is focused on template settings and the related fieldgroup/field definitions. However, it does not include the actual template files (i.e. PHP files) in the data. It's certainly feasible that it could (and we'll add it if there's sufficient demand), but the reality is that template files rarely exist on their own and usually have other includes or partials being referenced.

As a result, we think it's best to continue migrating your template files the same way that you do now. Though next week we'll likely be adding some file information to the template data so that it can alert you when it detects that the template files vary between the source and destination.

We hope that you enjoy using this tool and that it is a real time saver. However, you'll want to limit your use to non-production sites at present, as this feature is brand new. We appreciate your help testing–please let us know of any issues you run into.


### Change to how input fields collapse

In the past, there have been a few occasions where people are confused when they click on the label for an input field in ProcessWire, and it causes the field to close (or open). As a result, we have changed that behavior this week:

- If you click on the label for an open input, it focuses the input (where applicable). This is more consistent with the behavior that I think people expect from open inputs. It's also more consistent with how labels are supposed to work with inputs in general. You might also notice the arrow icon in the far right side of the label pulsates when you do this. That is there just to tell you that you can close the input by clicking on that arrow (should that be your intention).
- If you click on the label for a closed input, it opens the field and then focuses it (where applicable). For consistency, and so as not to confuse anyone: once a label has been used to open a field, it can also be used to close a field.
- The small arrow on the far right of every input field can always be used to open or close the input.
- A new "visibility" mode has been added to the field input configuration. This new mode (called Inputfield::collapsedNever, from the code side) is an option for those that want inputs that can never be closed.


### More CKEditor upgrades

With CKEditor being our new default rich text editor, we're continuing to upgrade and tweak it. This week we added support for custom configuration properties and custom configuration files. Now you can literally customize any CKEditor property possible.

- When editing the settings for a textarea field using CKEditor, go to: Input > CKEditor Settings > Custom Config Options. Here you can specify `property: value` pairs for any CKEditor setting. For an example, if you want to make your CKEditor interface bright blue, enter `uiColor: #438ef0`.
- If you prefer to keep your CKEditor config settings in a file, you can use [config.js](https://github.com/ryancramerdesign/ProcessWire/blob/dev/site-default/modules/InputfieldCKEditor/config.js).
- If you prefer to keep your CKEditor config settings in a file, and specify different settings for each of your CKEditor fields, create a file just like the one mentioned above, but append the field name to the filename, like this: config-body.js (for a field named "body"). See our example [config-body.js](https://github.com/ryancramerdesign/ProcessWire/blob/dev/site-default/modules/InputfieldCKEditor/config-body.js).


### New download capabilities in WireHttp class

When you download a module from the modules directory or ZIP file into your site, it uses the `WireHttp::download()` method. This download method is also available for your own use.

However, there were some instances where it wouldn't work due to server capabilities or PHP configuration, etc. For instance, some web hosts have PHP's `allow_url_fopen` option disabled, which would affect the ability to download in WireHttp.

This week we've added two new download methods to the class, ensuring that it can work on most, if not all, servers. First it attempts to use *cURL*. If that doesn't work, it falls back to *fopen*. Finally, if that doesn't work, it falls back to *sockets*. Hopefully with these additions, you'll always be able to use the download feature regardless of server.
