;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "fig5.2_homoDefor"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("tikz" "") ("amsmath" "")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone12"
    "tikz"
    "amsmath")
   (LaTeX-add-xcolor-definecolors
    "refblue"
    "refbluefill"
    "currteal"
    "currtealfill"
    "mappingred"
    "circgray"
    "axiscolor"))
 :latex)

