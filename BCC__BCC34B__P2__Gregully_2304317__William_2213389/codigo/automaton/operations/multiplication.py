from automata.tm.dtm import DTM

dtm_mult = DTM(
  states={"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "ha"},
  input_symbols={"1", "*"},
  tape_symbols={"E", "Z", "#", "*", "1"},
  transitions={
    "q0": {
      "#": ("q1", "#", "R")
    },
    "q1": {
      "1": ("q2", "#", "R")
    },
    "q2": {
      "*": ("q3", "1", "R"),
      "1": ("q5", "1", "R")
    },
    "q3": {
      "Z": ("q3", "1", "R"),
      "1": ("q3", "1", "R"),
      "#": ("q4", "#", "L")
    },
    "q4": {
      "1": ("ha", "#", "N")
    },
    "q5": {
      "1": ("q5", "1", "R"),
      "*": ("q6", "*", "R")
    },
    "q6": {
      "1": ("q7", "E", "R"),
      "Z": ("q9", "Z", "L")
    },
    "q7": {
      "Z": ("q7", "Z", "R"),
      "1": ("q7", "1", "R"),
      "#": ("q8", "Z", "L")
    },
    "q8": {
      "1": ("q8", "1", "L"),
      "Z": ("q8", "Z", "L"),
      "E": ("q6", "E", "R"),
    },
    "q9": {
      "E": ("q9", "1", "L"),
      "*": ("q10", "*", "L")
    },
    "q10": {
      "1": ("q10", "1", "L"),
      "#": ("q1", "#", "R")
    }
  },
  initial_state="q0",
  blank_symbol="#",
  final_states={"ha"}
)

# dtm_mult.read_input("#11*111####").print()
# dtm.read_input("#EE-E#").print()
# dtm.read_input("#E-EE#").print()
