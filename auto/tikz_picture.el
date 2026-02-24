;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "tikz_picture"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "tikz" "border={20pt 1pt 20pt 1pt}")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"))
 :latex)

