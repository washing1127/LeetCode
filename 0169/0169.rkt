; Author: washing
; DateTime: 2021/1/26 18:46
; File: 0136.rkt
; Desc: 

(define/contract (majority-element nums)
  (-> (listof exact-integer?) exact-integer?)
    (define a 0)
    (define c 0)
    (for ([n nums])
        (if (= 0 c) (set!-values (a c) (values n 1))
            (if (= a n) (set! c (+ c 1))
                (set! c (- c 1))))
    )
    a
  )