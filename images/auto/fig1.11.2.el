;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "fig1.11.2"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "tikz" "border={2cm 1pt 2cm 1pt}")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "amsmath"
    "bm"
    "tikz-3dplot"))
 :latex)

