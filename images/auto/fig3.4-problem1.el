;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "fig3.4-problem1"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "tikz" "border=14pt")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "tikz"
    "tikz-3dplot"
    "amsmath"))
 :latex)

