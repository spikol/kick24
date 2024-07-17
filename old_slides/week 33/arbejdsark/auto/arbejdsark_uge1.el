(TeX-add-style-hook
 "arbejdsark_uge1"
 (lambda ()
   (TeX-run-style-hooks
    "wrapfig")
   (LaTeX-add-counters
    "handout"))
 :latex)

