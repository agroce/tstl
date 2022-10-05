#lang plai-typed

(define-type FunDefC
  [fdC (name : symbol) (arg : symbol) (body : ExprC)])

(define-type ExprC
  [numC (n : number)]
  [idC (s : symbol)]
  [plusC (l : ExprC) (r : ExprC)]
  [multC (l : ExprC) (r : ExprC)]
  [ifC (c : ExprC) (t : ExprC) (f : ExprC)]
  [appC (fun : symbol) (arg : ExprC)])

(define (get-fundef [n : symbol] [fds : (listof FunDefC)]) : FunDefC
  (cond
    [(empty? fds) (error 'get-fundef "reference to undefined function")]
    [(cons? fds) (cond
                   [(equal? n (fdC-name (first fds))) (first fds)]
                   [else (get-fundef n (rest fds))])]))

(define-type Binding
  [bind (name : symbol) (val : number)])
 
(define-type-alias Env (listof Binding))
(define mt-env empty)
(define extend-env cons)

(define (lookup [id : symbol] [env : Env]) : number
  (cond
    [(empty? env) (error 'lookup "reference to undefined id")]
    [(cons? env) (cond
                   [(equal? id (bind-name (first env)))
                    (bind-val (first env))]
                   [else (lookup id (rest env))])]))    

(define (subst [what : ExprC] [for : symbol] [in : ExprC]) : ExprC
  (type-case ExprC in
    [numC (n) in]
    [idC (s) (cond
               [(symbol=? s for) what]
               [else in])]
    [plusC (l r) (plusC (subst what for l) (subst what for r))]
    [multC (l r) (multC (subst what for l) (subst what for r))]
    [ifC (c t f) (ifC (subst what for c) (subst what for t)
                      (subst what for f))]
    [appC (f a) (appC f (subst what for a))]))    
    

(define (sub_interp [e : ExprC] [fds : (listof FunDefC)]) : number
   (type-case ExprC e
    [numC (n) n]
    [idC (s) (error 'idC "undefined identifier")]
    [plusC (l r) (+ (sub_interp l fds) (sub_interp r fds))]
    [multC (l r) (* (sub_interp l fds) (sub_interp r fds))]
    [ifC (c t f) (if (= (sub_interp c fds) 0)
                     (sub_interp f fds) (sub_interp t fds))]
    [appC (f a) (local ([define fd (get-fundef f fds)])
                              (sub_interp (subst (numC (sub_interp a fds))
                                             (fdC-arg fd)
                                             (fdC-body fd)) fds))]))

(define (interp [expr : ExprC] [env : Env] [fds : (listof FunDefC)]) : number
   (type-case ExprC expr
    [numC (n) n]
    [idC (n) (lookup n env)]
    [appC (f a) (local ([define fd (get-fundef f fds)])
                  (interp (fdC-body fd)
                          (extend-env (bind (fdC-arg fd)
                                            (interp a env fds))
                                      env)
                          fds))]
    [ifC (c t f) (if (= (interp c env fds) 0)
                     (interp f env fds) (interp t env fds))]
    [plusC (l r) (+ (interp l env fds) (interp r env fds))]
    [multC (l r) (* (interp l env fds) (interp r env fds))]
    ))
