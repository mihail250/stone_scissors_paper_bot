res = {tuple(sorted(('stone', 'paper'))): 'paper',
       tuple(sorted(('stone', 'scissors'))): 'stone',
       tuple(sorted(('scissors', 'paper'))): 'scissors'
       }

all = ['scissors', 'paper', 'stone']

key = tuple(sorted( [all[0], all[1]] ))

print(res[key])