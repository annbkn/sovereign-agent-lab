"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input -> calling to confirm a booking                                                                                                               
How many guests are you confirming for tonight's event?
Your input -> 160 guests                                                                                                                                 
And how many of those guests will need vegan meals?
Your input -> about 50 vegan                                                                                                                             
What is the agreed deposit amount in GBP?
Your input -> £200 deposit                                                                                                                               
Deposit verified: amount £200.0 is within the approved limit.
Booking confirmed. We look forward to your event tonight.
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input -> calling to confirm a booking                                                                                                               
How many guests are you confirming for tonight's event?
Your input -> 160 guests                                                                                                                                 
And how many of those guests will need vegan meals?
Your input -> about 50 vegan                                                                                                                             
What is the agreed deposit amount in GBP?
Your input -> £350 deposit                                                                                                                               
This deposit exceeds our pre-approved budget. I will have a manager call you back within 15 minutes.
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "This deposit exceeds our pre-approved budget."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input -> calling to confirm a booking                                                                                                               
How many guests are you confirming for tonight's event?
Your input -> 160 guests                                                                                                                                 
And how many of those guests will need vegan meals?
Your input -> what time does the train leave?                                                                                                            
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM identified that the user question was completely unrelated to the current
booking confirmation flow, explicitly refused to answer the train schedule
question, and immediately prompted to see if the user wanted to return
to the active flow.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Both architectures correctly refused the request, but they handled it
differently. LangGraph reasoned dynamically that it lacked the tools to check
train times and generated a helpful but custom refusal message. Rasa CALM used
an explicit, pre-written guardrail flow for out-of-scope interactions
to forcefully steer the conversation back to its predefined business flow.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested the cutoff guard by modifying the hour condition directly in Python
to always trigger (e.g. `if True:`), retrained the model, and ran
a conversation. The agent immediately stopped the flow and responded with
the escalation message about being unauthorized to speak with anyone else.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
This simplification trades absolute deterministic control over dialogue paths
for extreme flexibility and natural conversational understanding.
The LLM handles the messy, unpredictable human inputs
(like extracting numbers from text) which saves us from writing brittle regex.
However, we still use deterministic Python for the actual business logic
(like checking capacity or deposit limits) because those checks must be legally
and financially rigorous.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The setup cost buys you rigid structure and strict adherence to predefined
business processes. Unlike LangGraph, the CALM agent cannot hallucinate
new tools, invent workflows, or stray outside its flows. It forces
the conversation down a designated track. For high-stakes, auditable
confirmation calls, this limitation is actually a feature, guaranteeing
the agent won't make up terms or go off-script.
"""
