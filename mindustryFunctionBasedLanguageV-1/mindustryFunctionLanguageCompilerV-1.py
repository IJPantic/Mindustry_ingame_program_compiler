#mindutry Function-based Langauge Compiler V-1
#14.March, 2025.
#by Ivan Jonjic Pantic (IJPantic on github)
#free use and edit for whatever you want

#inputs from user
fileWrite=input('file that compiled code will save to(will write to): ')
fileRead=input('file with function based code(will be read from): ')

#reading from file
with open(fileRead, 'r') as file:
    functionCode = file.read()

#seperating each function from code
lineList=[]
line=''
for indexcodeline in range(len(functionCode)):
	char=functionCode[indexcodeline]
	if char!=';':
		if char!='\n' and char!=' ':
			line+=char
	else:
		lineList.append(line)
		line=''

#extracting function name from function
instructionList=[]
instruction=''
for indexCodeLine in range(len(lineList)):
	for charIndex in range(len(lineList[indexCodeLine])):
		char=lineList[indexCodeLine][charIndex]
		if char=='(':
			instructionList.append(instruction)
			instruction=''
			break
		else:
			instruction+=char

#extracting argument part from function
arg=''
argTuple=[]
argTupleList=[]
startFlg=False
for indexCodeLine in range(len(lineList)):
	for charIndex in range(len(lineList[indexCodeLine])):
		char=lineList[indexCodeLine][charIndex]
		if char==')':
			argTuple.append(arg)
			arg=''
			argTupleList.append(argTuple)
			argTuple=[]
			startFlg=False
			break
		if startFlg==True and char!=',':
			arg+=char
		if startFlg==True and char==',':
			argTuple.append(arg)
			arg=''
		if char=='(':
			startFlg=True

#variables and lists
variables={}
eachInstructionLenght=[]
pointerList={}
compiledCode=''

#defining functions for function-based langauge
instructionLenght={
	'var':1,
	'point':0,
	'goto':1,
	'op':1,
	'printf':2,
	'input1b':1,
}

#TODO: add your new functions here
def var(argTuple,pointerList,eachInstructionLenght):
	return 'set '+argTuple[0]+' '+argTuple[1]+'\n'

def goto(argTuple,pointerList,eachInstructionLenght):
	return 'jump '+str(pointerList.get(argTuple[0]))+' '+argTuple[1]+' x false\n'

def op(argTuple,pointerList,eachInstructionLenght):
	return 'op '+argTuple[0]+' '+argTuple[3]+' '+argTuple[1]+' '+argTuple[2]+'\n'

def input1b(argTuple,pointerList,eachInstructionLenght):
	return 'sensor '+argTuple[0]+' '+argTuple[1]+' @enabled\n'

def printf(argTuple,pointerList,eachInstructionLenght):
	return 'print '+argTuple[0]+'\n'+'printflush '+argTuple[1]+'\n'

def point(argTuple,pointerList,eachInstructionLenght):
	pointerList[argTuple[0]]=sum(eachInstructionLenght)
	return ''

#compiling functions into mindustry code
for indexCodeLine in range(len(instructionList)):
	argTuple=argTupleList[indexCodeLine]
	instruction=instructionList[indexCodeLine]
	eachInstructionLenght.append(instructionLenght[instruction])
	compiledCode+=globals()[instruction](argTuple,pointerList,eachInstructionLenght)

#writing to a file
with open(fileWrite, 'w') as file:
    file.write(compiledCode)
print('DONE!')

