;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "mmi_1_2024-08-20"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "") ("amsmath" "") ("tcolorbox" "") ("mdframed" "") ("array" "") ("caption" "") ("float" "")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "graphicx"
    "amsmath"
    "tcolorbox"
    "mdframed"
    "array"
    "caption"
    "float"))
 :latex)

