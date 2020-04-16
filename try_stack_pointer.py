from get_stack import OpStack
import opcode

# inspired by https://stackoverflow.com/questions/57142762/debug-the-cpython-opcode-stack


import sys 

def tracefunc(frame, event, arg):
    frame.f_trace_opcodes = True
    if event == 'opcode':
        opname = opcode.opname[frame.f_code.co_code[frame.f_lasti]]
        if opname == 'BINARY_ADD':
            stack = OpStack(frame)
            print(f'{stack[-2]} + {stack[-1]}')
    return tracefunc

def f(a, b, c): 
    return a + b

sys.settrace(tracefunc)
f(2, 3, 4)