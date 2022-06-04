from automata.tm.dtm import DTM

dtm_sub = DTM(
  states={"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "ha"},
  input_symbols={"E", "-"},
  tape_symbols={"E", "#", "-"},
  transitions={
    "q0": {
      "#": ("q1", "#", "R")
    },
    "q1": {
      "E": ("q2", "#", "R")
    },
    "q2": {
      "E": ("q2", "E", "R"),
      "-": ("q3", "-", "R")
    },
    "q3": {
      "E": ("q3", "E", "R"),
      "#": ("q4", "#", "L")
    },
    "q4": {
      "E": ("q5", "#", "L")
    },
    "q5": {
      "E": ("q6", "E", "L"),
      "-": ("ha", "#", "N")
    },
    "q6": {
      "E": ("q6", "E", "L"),
      "-": ("q7", "-", "L")
    },
    "q7": {
      "E": ("q8", "E", "L"),
      "#": ("ha", "#", "N")
    },
    "q8": {
      "E": ("q8", "E", "L"),
      "#": ("q1", "#", "R")
    }
  },
  initial_state="q0",
  blank_symbol="#",
  final_states={"ha"}
)

# dtm.read_input("#EE-EE#").print()
# dtm.read_input("#EE-E#").print()
# dtm.read_input("#E-EE#").print()
 