;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "fig1.11.3-members3d"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "tikz" "border=14pt")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "tikz"
    "tikz-3dplot"
    "amsmath")
   (LaTeX-add-xcolor-definecolors
    "mfill"
    "mfillD"
    "mfillT"
    "mline"
    "cfill"
    "cline"
    "dcol"
    "acol"
    "hfill"))
 :latex)

