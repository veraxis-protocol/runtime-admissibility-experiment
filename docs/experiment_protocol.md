# Experiment Protocol

## Objective

Demonstrate that static authorization and runtime admissibility produce different outcomes when institutional state changes between classification and reliance.

## Systems compared

### Static authorization engine

Evaluates only the `t0` classification state.

### Runtime admissibility engine

Evaluates all predicates against the current `t2` state.

## Success criterion

A valid experiment shows that, under a material state change, the static engine may approve while the runtime admissibility engine escalates or blocks.
