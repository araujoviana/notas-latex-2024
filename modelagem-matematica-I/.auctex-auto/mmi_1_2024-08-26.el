;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "mmi_1_2024-08-26"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "") ("amsmath" "") ("geometry" "") ("csquotes" "") ("tcolorbox" "") ("svg" "")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "graphicx"
    "amsmath"
    "geometry"
    "csquotes"
    "tcolorbox"
    "svg"))
 :latex)

