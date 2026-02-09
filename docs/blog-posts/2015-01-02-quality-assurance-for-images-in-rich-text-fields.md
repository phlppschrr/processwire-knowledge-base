# Quality assurance for images in rich text fields

Source: https://processwire.com/blog/posts/quality-assurance-for-images-in-rich-text-fields/

## Sections


## Quality assurance for images in rich text fields

2 January 2015 by Ryan Cramer [ 9 Comments](/blog/posts/quality-assurance-for-images-in-rich-text-fields/#comments)

Hope that everyone had a great New Year! It's been a busy week with traveling and family this week, so there's not much to reveal in this week's post… today is the only day I've been in the office all week. But we do have something new that I think you'll like. I think this update is best described in a problem/solution format…


### The problem

When using a rich text editor (like CKEditor or TinyMCE) in ProcessWire, you can add images directly into the text. In fact, this is a very common thing, and something that I often do in these blog posts too. The image can either be one on the current page, or you can select an image from another page. But once the markup is generated for that `<img>` tag in the rich text field, it is static and ProcessWire knows nothing about it. This creates a few problems:

- If the image is deleted, then the `<img>` tag pointing to it is still in place. The result is a broken image.
- There's no way for the site administrator to know if there are any of these broken images, short of looking for 404s in the site logs.
- If the description associated with the image is changed, that change is not reflected in the "alt" attribute of the image, unless you update it manually.
- There's no way to clean-out all image size variations without also potentially breaking images in rich text fields.

As a markup-agnostic system, ProcessWire is not intended to solve all markup issues. But ProcessWire *is* intended to manage content, and what's described above is a content management problem that can only grow as scale increases. It's a problem that I think needs a built-in solution, even if it does get into the land of static markup.


### The solution

As of today's commits to the dev branch, if you edit the field settings for a textarea field and click on the details tab, you'll see a new Content Type option called "Markup/HTML with image management". If you choose that option, ProcessWire will keep track of any images referenced in the markup. Here's what it does:

- Populates blank alt attributes with file description, at runtime. This ensures any changes to the file description are reflected in the image alt attribute (multi-language aware too, of course).
- Automatically re-creates image size variations that do not exist. This enables you to delete all your image size variations (perhaps to clean things up) and know that anything still in use will be automatically re-created as needed.
- Automatically removes `<img>` tags that point to files that do not exist, so that front-end users won't ever see broken images. The broken image will still appear on the admin side, so that editors can easily find and correct it.
- Record missing image errors to a log file (called markup-qa-errors.txt).
- Send notifications to system/admin user if any broken images are found (as well as current editing user, if applicable). This part requires that you also have the *SystemNotifications* module installed.

All of this works regardless of whether the referenced image is on the current page or on another page. This is most likely to be useful on your typical *body* copy text field. If you'd like to take advantage of this feature, grab the latest dev branch and go to Setup > Fields and edit any of your textarea fields. Click on the Details tab and select "Markup/HTML with image management" for the *Content Type* and save.


### Why isn't this feature a Textformatter module?

This feature actually did start out as a Textformatter module, but I later decided it really should be built-in to the Textarea Fieldtype for a few reasons.

- This is something that you probably want on all Textarea fields that could potentially contain images. This is about quality assurance and making sure content isn't broken, in the same way that the existing Markup/HTML option is… we're just expanding upon what it does.
- While there is some text formatting going on here (inserting alt attributes and removing non-existent images), there's more than that. We're keeping track of image references, making sure they exist, re-creating image variations, and notifying administrators of problems.
- Lastly, we want the problem checks to run regardless of whether the page has output formatting enabled or not. Textformatter modules only run on the front-end of your site in output formatting mode. We want our problem checks to run even if you are in the admin.


### Are there any drawbacks to using this?

There is minimal overhead associated with performing these checks. If the page has no img tags present, then there is no overhead at all. If there are img tags present, then the overhead is simply limited to locating the img tags and making sure the files exist.
