(defmacro setTo10(num)
    "Documentación: Setea el parametro a 10 en el Macro"
    (print "Antes de: ")
    (write num)
    (setq num 10)
    (print "Despues de: ")
    (write num)
)
(setq x 25)
(print x)
(write-line "")
(setTo10 x)
(print "Despues de función: ")
(write x)