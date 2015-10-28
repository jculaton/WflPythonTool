import time
import random
import string

target = raw_input("Target String: ")
possibleCharacters = string.ascii_letters + string.digits + "!@#$%^&*():?><,.{}[]/;"
#target = "The courts have shown interest in any clues they can find in the Preamble regarding the Constitution's meaning.[6] Courts have developed several techniques for interpreting the meaning of statutes and these are also used to interpret the Constitution.[7] As a result, the courts have said that interpretive techniques that focus on the exact text of a document[8] should be used in interpreting the meaning of the Constitution. Balanced against these techniques are those that focus more attention on broader efforts to discern the meaning of the document from more than just the wording;[9] the Preamble is also useful for these efforts to identify the spirit of the Constitution.Additionally, when interpreting a legal document, courts are usually interested in understanding the document as its authors did and their motivations for creating it;[10] as a result, the courts have cited the Preamble for evidence of the history, intent and meaning of the Constitution as it was understood by the Founders.[11] Although revolutionary in some ways, the Constitution maintained many common law concepts (such as habeas corpus, trial by jury, and sovereign immunity),[12] and courts deem that the Founders' perceptions of the legal system that the Constitution created (i.e., the interaction between what it changed and what it kept from the British legal system[13]) are uniquely important because of the authority the People invested them with to create it.[14] Along with evidence of the understandings of the men who debated and drafted the Constitution at the Constitutional Convention, the courts are also interested in the way that government officials have put into practice the Constitution's provisions, particularly early government officials,[15] although the courts reserve to themselves the final authority to determine the Constitution's meaning.[16] However, this focus on historical understandings of the Constitution is sometimes in tension with the changed circumstances of modern society from the late 18th century society that drafted the Constitution; courts have ruled that the Constitution must be interpreted in light of these changed circumstances.[17] All of these considerations of the political theory behind the Constitution have prompted the Supreme Court to articulate a variety of special rules of construction and principles for interpreting it.[18] For example, the Court's rendering of the purposes behind the Constitution have led it to express a preference for broad interpretations of individual freedoms.[19]"
currentAttempt 	= ""
nextAttempt 	= ""
mutations = 1


for i in range(len(target)):
	currentAttempt+= random.choice(target)

targetReached = False

while targetReached == False:
	nextAttempt = ""
	targetReached = True
	print("(" + str(mutations) + ") " + currentAttempt)
	for i in range(len(target)):
		if currentAttempt[i] != target[i]:
			nextAttempt+= random.choice(target)
		else:
			nextAttempt+= currentAttempt[i]
	currentAttempt = nextAttempt
	if currentAttempt != target:
		targetReached = False
		mutations += 1
	time.sleep(.05)

print(currentAttempt)
print("Target reached!")
print("# of mutations: " + str(mutations))