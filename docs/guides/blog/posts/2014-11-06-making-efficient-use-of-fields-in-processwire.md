# Making efficient use of fields in ProcessWire

Source: https://processwire.com/blog/posts/making-efficient-use-of-fields-in-processwire/

## Sections


## Making efficient use of fields in ProcessWire

6 November 2014 by Ryan Cramer [ 4 Comments](/blog/posts/making-efficient-use-of-fields-in-processwire/#comments)


## Optimize field use

In ProcessWire there is no set limit on how many custom fields you can create. But fields are not meant to scale infinitely in the way that pages are. Thousands of fields will not scale as well as thousands of pages (for the system or for you). In this article we'll attempt to outline some of the best practices for making efficient use of fields in ProcessWire and how to optimize your use.

Consider the following:

- Every field you create represents an additional variable you [the developer] has to keep track of. Sites with fewer fields are easier to maintain over time, and easier to collaborate on with other developers.
- The fewer fields you have, the more reusable your output code tends to be. If your fields tend to be more general purpose rather than template-specific, you'll be able to write reusable code that can output a broader range of page types.
- ProcessWire loads data for fields on-demand. If you've got 200 fields on a template and your page is outputting all of them, that will take longer than if your page had 50 fields. The more fields you have in your system, the more potential memory usage and overhead on the server. Granted you may not be able to tell, but the point is that every field takes up a little bit of space in memory.

Given these factors, here are some things you can do to optimize the use and quantity of fields necessary to meet the needs of your site or application.


### Use Page fields rather than individual checkboxes

I very often see sites that contain a lot of individual checkbox fields for various toggles for things that can be turned on or off on a page. These are great for that purpose, but if you get to the point of having 3 or more of them (or want to plan for more) you may be better off using a Page field instead.

Using a page field, you can convert any number of checkbox toggle fields into a single Page field:

- Create your checkbox options as pages somewhere in your site structure. I usually create a hidden /tools/ page in my site for this kind of stuff, and then might keep my checkbox options as pages below /tools/toggles/, for example. My checkbox pages"typically all use a template with nothing but a "title" field, which is used for the checkbox labels.
- Create a new Page field, perhaps naming it "toggles". Accept the default PageArray type on the Details tab. On the Input tab, set the parent to be /tools/toggles/ (or wherever you created them). Also on the Input tab, you can select the type of input you want it to use, which in this case would be "checkboxes".
- Add that new "toggles" Page field to one or more templates. Now when you edit any pages using those templates, you have a new field with all your checkbox toggles. The fact that it looks better and takes up less space than having separate checkbox fields is icing on the cake.

Your next question might be how to use it on the front-end of your site? It's a little different than how you'd use individual checkbox fields, but it's also more flexible. Because the value of the checkbox field is just a PageArray, there are any number of ways to see what it contains, but I usually like to refer to the "name" property because it remains easily readable in the code. As an example, lets say that I wanted to check if a toggle named "featured" is set on the current page:

```
if($page->toggles->get("name=featured")) {
  // this page has the "featured" toggle set
}
```

Another case might be that you just want to render a list of all toggles active for the current page. In this case, we'll use the "title" of each toggle since it's formatted better for reading:

```
foreach($page->toggles as $toggle) {
  echo $toggle->title . "<br>";
}
```

And another alternative for those that like less-readable 1-line statements:

```
echo $page->toggles->implode("<br>", "title");
```

To reiterate, you can combine any number of individual checkbox fields into a single Page field. If you are replacing a lot of individual checkboxes, this can be significantly more efficient, not to mention easier to scale and maintain.


### Use multi-file fields to replace several single-file fields

If you are using a lot of separate single-file fields in a given template, consider combining them all into just one multi-file field, and enable the "tags" option. By "multi-file", I mean setting your files field to have no maximum (specified by "0"), and setting the "Formatted Value" to be "Automatic" or "Array", both visible on the Details tab when editing your files field. The tags option can also be seen here, under "Use Tags?". Check the box to use tags and you now have a way to specify what each file in that field is for.

Lets say that you were building a website selling homes and you want to separately identify which photos are for inside and outside the home (interior and external). You might like to go further and separately identify kitchen, bathrooms, bedrooms, etc., but lets just focus on inside and outside for the moment. Do note however that you can have any number of tags for each file. When uploading files to your files field, you can designate each photo as interior or external just by entering the tag "interior" or "exterior". Typically you'd instruct the user uploading files on what tags they should use in your file field's description.

On the front-end of your site, you could output all the interior photos as a group and all the exterior photos as a group, while still having them all in the same files field. Here's how:

```
echo "<h3>Exterior Photos</h3>";
foreach($page->photos->findTag("exterior") as $photo) {
  echo "<img src='$photo->url' alt='$photo->description' />";
}
echo "<h3>Interior Photos</h3>";
foreach($page->photos->findTag("interior") as $photo) {
  echo "<img src='$photo->url' alt='$photo->description' />";
}
```

Lets say that you also wanted to let the editor designate one of the photos as the big cover photo at the top of the page, using the tag "cover". If there was no photo with that tag, then you'd just use the first photo.

```
$cover = $page->photos->getTag("cover");
if(!$cover) $cover = $page->photos->first();
echo "<img src='$cover->url' alt='$page->title' />";
```


### Create general-purpose fields and re-use them (where it makes sense)

If you've got similar fields across multiple templates (in terms of what is stored and input), consider using a general purpose field across multiple templates rather than separate template-specific fields. Most of our site profiles include fields like "title", "body" and "summary", which are good examples of this. Avoid using single-template specific fields, like "product_body", "company_summary", etc. (when possible), because you can simply re-use a general purpose field shared across multiple templates.

For every field that you create, always think about the bigger picture and how you might utilize that field in a broader context across multiple templates, whether now or in the future. I'm not suggesting you start creating fields with names like textarea1, textarea2, textarea3, etc., as that would be entirely *too* general purpose and be unintelligible from the code side. But I do see a lot of instances where people create the same field over and over again separately for each template, and that definitely calls for more consideration of field reuse.

As a bonus, using more general purpose fields improves code reusability. If you've got a block of code that generates some output, it may be able to cover a broader range of page templates if there is some common ground in field names across templates.


### Use field template context

Do you ever find yourself creating new fields simply so that it can have a different label, description, required state, etc.? If so, there's no need to. ProcessWire provides you with something called *field template context* that lets you customize any aspects of the field as it's shown to the editor, separately for each template. Just for starters, you can have a field named "body" labeled as "Body Copy" in one template, and "Product Description" in another, and it's incredibly easy to do.

To use field template context, go and edit any template (Setup > Templates > any template). Click on any of the field names shown in the template and it will pop up a window that enables you to customize several aspects of that field that only apply within the context of the template you are editing.


### Use PageTable and Repeaters

ProcessWire comes with two separate Fieldtypes that let you create repeatable blocks of fields: PageTable and Repeaters. We could write an entire book on all that you can do with these, so rather than getting too far into it here, we'd suggest that you experiment and see the potential yourself. Neither of these are installed by default, but they do come with the core. Simply go to Modules > Core > Fieldtype and install them both. Once installed, usage is fairly self explanatory, but take your time and explore, as there is a lot of power and likewise potential for efficiency.

Repeaters are a little easier to configure initially, but PageTable fields are ultimately more powerful. If you don't want to learn them both, then focus in on PageTable. In either case, the repeatable items in each of these fields are themselves pages that can contain any group of fields you desire. PageTable goes even further and enables you to have a single PageTable field that can publish pages using different templates from within the same field.


### Use ProFields

[ProcessWire ProFields](https://processwire.com/talk/store/product/10-profields/) is one of our commercial modules that is designed specifically for the purpose of letting you do more with fewer fields. Because a lot has been written on these already, I will link to the relevant information rather than repeat it here:

- [Textareas](https://processwire.com/api/modules/profields/textareas/) The Textareas Fieldtype and Inputfield lets you combine multiple named text fields into a single field. Now with native multi-language support too.
- [Multiplier](https://processwire.com/api/modules/profields/multiplier/) This Fieldtype and Inputfield combination lets you take almost any existing single-value Fieldtype, and use it to a multi-value Fieldtype.
- [Table](https://processwire.com/api/modules/profields/table/) This Fieldtype is the first of its kind in that it lets you literally define your own Fieldtype. Think of it kind of like a lean and mean repeater field, with no extra overhead.


### Create your own Fieldtypes and Inputfields

You can meet any data storage or input need by creating your own fields. After all, ProcessWire fields are just plugin modules, and you can always create your own custom modules to meet your specific needs. Admittedly, this is not for everyone, but if you don't mind getting your hands a little dirty with some PHP, you can literally do anything. In fact, ProcessWire was designed from the beginning to be extended in just this way.

As an example of how a custom Fieldtype/Inputfield might be beneficial in reducing fields, consider what it takes to represent an individual's contact information. You may need separate fields for: first_name, last_name, phone, email, company, address1, address2, city, state, zip, and country, and maybe more. That's at least 11 separate fields that could be represented by a single custom aggregate field. This can be accomplished relatively easily by creating a custom Fieldtype to manage and store the data, and a a custom Inputfield to provide input for it in the admin.

What it takes to create custom Fieldtypes and Inputfields is beyond the scope of this document, but there are numerous examples both in the core and 3rd party for you to look at. We've also created a custom one called the [Events Fieldtype](http://modules.processwire.com/modules/fieldtype-events/) purely for demonstration purposes.

If you have a custom field need, but don't feel comfortable creating your own, post in our [jobs board](https://processwire.com/talk/forum/22-jobs/) and you'll be able to find someone that would be happy to create it for you.

What other ways have you found work well in making efficient use of fields in ProcessWire? This article just covers a few things, but there are certainly more possibilities.
