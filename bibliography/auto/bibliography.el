;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "bibliography"
 (lambda ()
   (LaTeX-add-bibitems
    "stallings2006esp"
    "stallings2022computer"))
 '(or :bibtex :latex))

