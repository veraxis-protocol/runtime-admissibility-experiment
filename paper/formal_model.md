# Formal Model

Let:

- `x` denote a proposed machine-generated action.
- `t0` denote classification time.
- `t2` denote reliance or execution time.
- `S_t` denote institutional state at time `t`.
- `A_t` denote the authority envelope at time `t`.
- `E_t` denote the evidentiary basis at time `t`.
- `C` denote the consequence class.
- `Rel(x,t)` denote institutional reliance on action `x` at time `t`.
- `RA(x,t)` denote runtime admissibility of action `x` at time `t`.

Institutional reliance requires runtime admissibility:

```math
Rel(x,t) \Rightarrow RA(x,t)
```

Defective reliance:

```math
Rel(x,t) \land \neg RA(x,t)
```

Runtime admissibility:

```math
RA(x,t) \Leftrightarrow
VA(x,A_t) \land SE(x,E_t) \land CS(x,S_t) \land WS(x,A_t,C)
\land CB(x,C) \land EI(x,t) \land COR(x,C)
```
