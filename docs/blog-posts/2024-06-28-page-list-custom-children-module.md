# Page List Custom Children module

Source: https://processwire.com/blog/posts/page-list-custom-children-module/

## Sections


## Introducing the “Page List Custom Children” module

28 June 2024 by Ryan Cramer [ 0 Comments](/blog/posts/page-list-custom-children-module/#comments)

This simple module gives you the ability to customize the parent/child relationship as it appears in the admin page list, enabling child pages to appear under more than one parent.

Having more than one path to pages in the admin page list can make pages easier to find. It also enables you to increase consistency between admin and front-end navigation structures. Below is a screenshot of this module in action. Though in this post, we'll use another example to walk you through how it works and how to use it.


### How it works, by example

The simplest use case for this module might be a blog, and this serves as a good introduction for how this module might come in handy. On the front-end site for a blog, usually there's more than one path to get to a blog post. Paths might include: by date, by category, by author, etc. So let's consider the following page structure common for blogs in ProcessWire:

```
/blog  /blog/posts    /blog/posts/my-favorite-foods    /blog/posts/some-nice-cars    /blog/posts/good-pizza-recipes  /blog/categories    /blog/categories/food    /blog/categories/cars  /blog/authors    /blog/authors/ryan    /blog/authors/karen
```


### A common blog scenario

On the front-end of the site, browsing the `/blog` or `/blog/posts` pages would likely show a chronological list of blog posts or summaries.

Browsing `/blog/categories/food` would show all posts in the category "Food".

And browsing `/blog/authors/karen` would show all posts authored by Karen.


### Translating that scenario to the admin page list

What if we could make this front-end behavior (described above) also work in the admin page list? That's what this module does. While a blog is used to demonstrate (since it's likely familiar to most) it's just one of many potential use cases.

In this example, blog posts have the template `blog-post`, categories have the template `category` and authors have the template `author`. The blog-post pages have Page reference fields named categories and author, enabling one to create the relationships between blog-posts, categories, and authors.

Without this module, if we navigate in the admin page tree to: Blog > Categories > Food, that's the end of the line, as there are no children below the "Food" category. But with this module, we can make the page list show the `blog-post` pages in the "Food" category as children of the Food category page.


### Here's how we'd configure that in the module settings

```
template=category >> parent=/blog/posts, categories=page.id
```

Here we have 2 different selectors separated by `>>`. It's a kind of "if" statement, where the first selector is the condition, and the second is result (what finds the pages if the condition matches).

Note that we can refer to the page matched in the first selector by specifying `page.id` in the second selector.

With that rule added, we can now navigate to blog posts by category in the admin page list:

- Blog > Categories > Food > My favorite foods
- Blog > Categories > Food > Good pizza recipes

The `blog-post` pages didn't change parents, they still live under `/blog/posts`, but they are just re-appearing as children of the matching category pages.


### Narrowing the result

What if we just want to show blog posts created in the last 3 months as children of the category pages? Assuming each blog post has a date field, we might do this:

```
template=category >> parent=/blog/posts, categories=page.id, date>"-3 MONTHS"
```


### Showing posts below authors

Setting up posts to appear as children beneath each author page works pretty much the same as categories:

```
template=author >> parent=/blog/posts, author=page.id
```


### Merging children

What if we had a case where the page matched in the first selector already has some of its own children? What's present in our second selector will effectively replace what the page list usually shows.

So if our `author` pages already had some other kind of children (whatever they might be) we can have it show both those children and the posts they've authored by using a [OR group](/docs/selectors/#or-groups) in our second selector:

```
template=author >> (parent=/blog/posts, author=page.id), (parent=page.id)
```

The second selector above says "match pages with parent /blog/posts that have the author as the current page" **OR** "match pages that have the current page as the parent". That will result in both the actual children and authored blog posts appearing as children of the author.


### What about adding pages?

This module also updates the "new" page links that appear in the page list. So if you click to Blog > Categories > Food > *New*, it will know to add the new post in `/blog/posts` (rather than `/blog/categories/food/`).

Further, once the new page is created, it will have that "Food" category already populated in the categories field, since that's where you started adding the new page.


### Download and install

This module is available for download now in the ProcessWire modules directory here: [Page List Custom Children](/modules/page-list-custom-children/). Please consider version 1 to be a beta version.

To install, extract the files into /site/modules/PageListCustomChildren/, then go to Modules > Refresh in the admin. Click install for this module and then you'll be on the configuration screen, ready to go!
