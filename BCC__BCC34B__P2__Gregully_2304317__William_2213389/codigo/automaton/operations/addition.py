from automata.tm.dtm import DTM

dtm_add = DTM(
  states={"q0", "q1", "q2", "q3", "ha"},
  input_symbols={"E", "+"},
  tape_symbols={"E", "#", "+"},
  transitions={
    "q0": {
      "#": ("q1", "#", "R")
    },
    "q1": {
      "E": ("q1", "E", "R"),
      "+": ("q2", "E", "R")
    },
    "q2": {
      "E": ("q2", "E", "R"),
      "#": ("q3", "#", "L")
    },
    "q3": {
      "E": ("ha", "#", "N")
    }
  },
  initial_state="q0",
  blank_symbol="#",
  final_states={"ha"}
)

# dtm.read_input("#EEEEE+EE#").print()
