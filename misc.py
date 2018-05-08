
if not globals().has_key("g_FuncCall"):
        g_FuncCall = {}

def func_call(fn, *args, **kwargs):
        def _fn(*args, **kwargs):
                g_FuncCall[fn] = g_FuncCall.get(fn, 0) + 1
                return fn(*args, **kwargs)
        return _fn

def PrintFuncCall():
        for k, v in g_FuncCall.items():
                print "FuncCall", k.func_name, v

P_INF = float("inf")    #positive infinity
N_INF = float("-inf")   #negative infinity
