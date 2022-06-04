from automata.tm.dtm import DTM

dtm_div = DTM(
  states={"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "ha"},
  input_symbols={"1", "/"},
  tape_symbols={"E", "Z", "#", "/", "1"},
  transitions={
    "q0": {
      "#": ("q1", "#", "R")
    },
    "q1": {
      "1": ("q2", "#", "R"),
      "/": ("q9", "#", "R")
    },
    "q2": {
      "1": ("q2", "1", "R"),
      "/": ("q3", "/", "R")
    },
    "q3": {
      "1": ("q3", "1", "R"),
      "E": ("q3", "E", "R"),
      "#": ("q4", "#", "L"),
      "Z": ("q4", "Z", "L")
    },
    "q4": {
      "E": ("q4", "E", "L"),
      "1": ("q5", "E", "L")
    },
    "q5": {
      "1": ("q7", "1", "L"),
      "/": ("q6", "/", "R")
    },
    "q6": {
      "E": ("q6", "1", "R"),
      "Z": ("q6", "Z", "R"),
      "#": ("q7", "Z", "L")
    },
    "q7": {
      "Z": ("q7", "Z", "L"),
      "1": ("q7", "1", "L"),
      "/": ("q8", "/", "L")
    },
    "q8": {
      "1": ("q8", "1", "L"),
      "#": ("q1", "#", "R")
    },
    "q9": {
      "Z": ("q9", "1", "R"),
      "1": ("q9", "#", "R"),
      "#": ("ha", "#", "N")
    }
  },
  initial_state="q0",
  blank_symbol="#",
  final_states={"ha"}
)

# dtm_division.read_input("#1111111/11####").print()
# dtm.read_input("#EE-E#").print()
# dtm.read_input("#E-EE#").print()
