# Starting a site with the “blank” profile

Source: https://processwire.com/blog/posts/starting-with-the-blank-profile/

## Sections


## Starting a site with the “blank” profile

10 June 2022 by Ryan Cramer [ 4 Comments](/blog/posts/starting-with-the-blank-profile/#comments)

ProcessWire 3.0.200+ comes with just 1 site installation profile, the *site-blank* profile. This profile makes very few assumptions, making it a minimal though excellent starting point. Here’s how you might use it.

While [other installation profiles](/download/site-profiles/) are available separately, there's a good chance that you will be starting with the included blank profile. The blank profile includes very little, meaning it likely doesn't have anything in it that you'll be throwing out. But it also won't have everything you'll likely need in order to start building out a site. So depending on the case, we may need to do a few things before we're really ready to start building a site with it. Here are some useful steps you might take when starting from the blank profile…


### Optimizing installation

In this section we'll take you through the installer, which is the first step towards creating a site in PW.

**DB Charset and Engine:** On the "MySQL database" screen I select `utf8mb4` for "DB Charset" and `InnoDB` for "DB Engine".

These are the optimal settings if supported by your MySQL version (5.6.4 or newer). Using the utf8mb4 character set is useful if you need to support languages that require it... but even if you don't, it's nice to have as it makes emojis possible in content as well. Sooner or later may clients end up asking why they can't use one emoji or another, so might as well plan for it at installation time and utf8mb4 ensures you are ready. ?

The **InnoDB engine** is preferable to the MyISAM engine because it enables ProcessWire to be safer and more efficient. Specifically, it enables it to use row locking rather than table locking (for better performance and scalability) and it enables PW to use transactions for some of its queries, making it potentially safer in some error situations. Though admittedly, MyISAM has never failed me either. But InnoDB has other benefits as well, so it's nearly always preferable unless your MySQL version is prior to 5.6.4.

On the **HTTP Host Names** input, I enter my localhost development host name (localhost:8888) as well as the server host names the site will eventually live at, i.e. domain.com and www.domain.com. If you don't know what those will be, you can always revisit it later in your /site/config.php `$config->httpHosts` setting.

For **Debug mode** I pretty much always start with this "Enabled". Unless you are going straight from installer to launch, you'll want to start with Debug mode enabled too. This ensures that PHP error messages are visible and not hidden behind an anonymous 500 server error.

After installation completes, click the button to "Login to admin" so that you can start adding modules and creating fields.


### What core modules to install

While the majority of modules that you will need are already pre-installed, there are a few that come with the core that aren't pre-installed, but that you may still want. Following is a list of additional core modules that I like to install first thing (I use them on just about every site I work with). While we won't use all of them initially, chances are that you'll come across a need for them at some point during your site development, so it makes sense to go ahead and install them now. To install, locate them in the admin via: Modules > Install.


### Fieldtype modules

- **Select Options:** Enables various selection types independent of Page fields.
- **Repeater:** Build repeatable groups of fields.
- **Toggle (Yes/No):** Useful alternative to Checkbox fields.


### Inputfield modules

- **Page Auto Complete:** A useful input option for Page fields
- **Text Tags:** Another useful input option for Page fields


### Page modules

- **Page Path History:** Makes PW remember where pages have lived so that it can automatically update links and perform redirects.
- **Page Paths:** Enables page paths/urls to be queryable by selectors. Also offers potential for improved load performance.


### Process modules

- **Forgot Password:** Enables a "forgot password" option on the login screen (install only if needed).
- **Page Clone:** Provides ability to clone/copy/duplicate pages in the admin. Adds a "copy" option to all applicable pages in the PageList.


### Image modules

- **IMagick Image Sizer:** When supported by the server it can often be preferable to PHP's default GD image sizer engine.

There are also some 3rd party and Pro modules that I often like to install at this stage too, but for now let's start with just what the core gives us, which is plenty.


### What fields to create

The blank profile comes with just 1 visible field: "title". There are a certain few other fields that I know I'll need on just about every installation, so here's what fields I almost always add right away:


### body

*Type: Textarea/CKEditor*

Just about every site needs a field to contain text for body copy. I almost always use a textarea field with CKEditor as the input type. To do this, go to Setup > Fields > Add New, and create a new field named "body" with "Textarea" selected as the type.

On the "Details" tab, for "Inputfield Type" select "CKEditor". For "Content Type" select "Markup/HTML". It will reveal "Markup/HTML" settings box — I usually just check the box for "Link abstraction", though review the options and see what suits you.

Save and then click to the "Input" tab, which reveals all the CKEditor settings. The defaults here are a good starting point, but it's good to know what's there for when/if you need to later change something.


### headline

*Type: Text*

The built-in "title" field typically serves as both a page's navigation title and headline. But I've found on most sites that some pages inevitably need a longer version of the title for the page's headline. For instance, the page title might be "FAQ" but the headline is "Frequently Asked Questions". So this is a field I usually create from the get-go.

After creating the "Text" field named "headline", on the "Details" tab for "Text formatters" be sure to select "HTML Entity Encoder". This ensures the output is prepared and safe for HTML.

On the "Input" tab, for "Visibility" select "Open when populated + Closed when blank". Since I consider this field optional, this ensures the field is collapsed in the page editor unless/until we need it.


### browser_title

*Type: Text*

This field is mostly identical in configuration to the "headline" field (described above) but I reserve it for use in the `<title>` tag output that appears in the `<head>` section of the HTML document. This is important for search engines as it is what they display as the linkable text in your search engine listings (like at Google). Like with the headline field, I consider this optional and so fallback to the title field when it is not present. You'll see how to do this when we edit the _main.php template file further down below.

This field is created the same way as the headline field mentioned above. But because `<title>` field content is ideally kept to a maximum of 60 characters, I write in the "description" or "notes" something like "Try to keep the length no longer than 60 characters". This is a soft limit or recommendation, not a hard requirement.

When editing the field, on the "Input" tab, under the "Counter" setting, I select "Character counter", so that the editor will see how many characters long their browser_title is, making it easy for them to match the 60 character max recommendation. The browser_title has search keyword value in that it carries weight in matching words or phrases the user searches for. It also has marketing value in that it sells the user to click on your site (or not) from the search engine result pages.


### meta_description

*Type: Text*

This field holds summary text for the page and is what populates the `<meta name="description" content="...">` in the document `<head>`. It is used by search engines to provide additional description in the search engine results. It has the same user marketing value as the browser_title, but matching keywords in searches are not as important here.

I create this field exactly like the browser_title field except that in the description or notes I mention that a maximum character count of 160 is recommended (though not required).


### images

*Type: Images*

Chances are you'll need an images field for uploading files to, whether for our own layout purposes, or for supporting images placed in your "body" field. To do this, create a new "Images" field named "images". Save.

On the "Details" tab, the only thing you'll likely want to do at first is determine whether or not you'll be supporting image file descriptions (text describing a file, like you might use in an alt attribute). If you don't want image descriptions, set the "Number of rows for description field" to 0. Or if you *do* want image file descriptions, then select "HTML Entity Encoder" for the "Text formatters", ensuring that description is ready for use in HTML and/or alt attribute.

Another setting I almost always use for image fields is on the "Input" tab in the "Maximum image dimensions" fieldset. I like to enter a "Max width for uploaded images" of "1600" for client-side resize. This ensures that if the client uploads an image straight off their DSLR camera that we won't store that unnecessarily large image on the server.


### image

*Type: Images (max files 1)*

In addition to the above Images field, I usually create another one exactly like it except that it is named "image" (non-plural) and is configured to hold just 1 image. This is what I use for pages that need a single header/hero image. But even if I don't have such an immediate need, I know I'll eventually need a single image field for one purpose or another, whether for a page, within a repeater, or any number of other things. So I'll usually go ahead and create that single "image" field right now at the beginning.

Since it differs from the "images" (plural) field in only one way, I'll clone that "images" field when creating my new "image" field. Do this by going to Fields > Add New Field, enter "image" for the label/name, and then for the "Type" dropdown, select the "images" field to clone that existing field. (You'll see the clone option at the bottom of the Select). Once created, click on the "Details" tab and for "Maximum number of files", enter "1" — this is what differentiates it from your images (plural) field. Save.


### Setting up templates

The blank profile comes with just 2 templates: home and basic-page. Most often, this is all I need to get things started. Though we do need to add those fields created earlier to these templates. Go to Setup > Templates > basic-page (or home) and add fields in this order (or a different order if you prefer):

- title
- headline
- body
- Images
- browser_title
- meta_description


### Modifying template files for the new fields

The template files in /site/templates/ serve as good starting points, but at minimum we want to update them to support a couple of the fields we created. To start with, I'll update the _main.php template file `<head>` section to support our new browser_title and meta_description fields:

```
<head id="html-head">
  <title><?=$page->get('browser_title|title')?></title>
  <?=$page->if("meta_description", "<meta name='description' content='{value}' />")?>
</head>
```

Note that in the case of "browser_title", it falls back "title" when the browser_title is blank. But for the "meta_description", we use `$page->if(…)` to render that meta tag only if it is populated (skipping it if it is blank). Also, just in case it's not obvious, I've omitted the other stuff in the <head> tag, so my example focuses just on what's been changed or added.

In the document `<body>` we update our `<h1>` tag to output headline when populated, or title when not:

```
<h1 id="headline">
  <?=$page->get('headline|title')?>
</h1>
```

Now let's edit both the home.php and basic-page.php template files. Both of them have nothing other than a `div#content` with some static text. Because the blank profile uses [markup regions](/docs/front-end/output/markup-regions/), this means the div#content automatically replaces the one that appears in the _main.php file. Let's change that to output our `$page->body` instead:

```
<div id="content">
  <?=$page->body?>
</div>
```

With these template file changes above, we've got a worthwhile starting point to start building pages, editing content, and previewing it on the front-end.


### Things to note about the blank profile

The blank profile is setup with a few useful defaults. Any of these can be toggled in the /site/config.php file.


### Next steps

What's next? Depending on the site, next steps might include:

- Adding in relevant 3rd party or Pro modules
- Enabling WebP image support
- Enabling multi-language support
- Enabling front-end editing support
- Adding a front-end framework like Uikit
- Optimizing settings in /site/config.php

If you'd like to read a part 2 to this article that includes some of those steps above (and more) please let me know.

What other steps do you take when starting from the blank profile? Please let us know below and thanks for reading!
