# $pages->uncacheAll(?Page $page = null, array $options = array()): int

Source: `wire/core/Pages.php`

Remove all pages from the cache (to clear memory)

This method clears all pages that ProcessWire has cached in memory, making room for more pages to be loaded.
Use of this method (along with pagination) may be necessary when modifying or calculating from thousand of pages.

~~~~~
// calculate total dollar value of all 50000+ products in inventory
$total = 0;
$start = 0;
$limit = 500;

do {
  $products = $pages->find("template=product, start=$start, limit=$limit");
  if(!$products->count()) break;
  foreach($products as $product) {
    $total += ($product->qty * $product->price);
  }
  unset($products);
  $start += $limit;
  // clear cache to make room for another 500 products
  $pages->uncacheAll();
} while(true);

echo "Total value of all products: $" . number_format($total);
~~~~~

## Arguments

- Page|null $page Optional Page that initiated the uncacheAll
- array $options Options to modify default behavior: - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent that call, set this to true.

## Return value

int Number of pages uncached
