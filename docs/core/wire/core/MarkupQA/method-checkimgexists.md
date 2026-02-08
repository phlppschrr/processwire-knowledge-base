# MarkupQA::checkImgExists()

Source: `wire/core/MarkupQA.php`

Attempt to re-create images that don't exist, when possible

@param Pageimage $pagefile

@param $img

@param $src

@param $value

@return int Returns 0 on no change, negative count on broken, positive count on fixed
