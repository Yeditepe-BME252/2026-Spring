;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "fig2.4.1"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "tikz" "{2cm 1pt 2cm 1pt}")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "tikz"
    "amsmath"
    "bm")
   (TeX-add-symbols
    "theta"
    "L"))
 :latex)

