is_rd = False
if is_rd:
    state_msg = 'Ready'
else:
    state_msg = 'You are non repaired!!!'

print(state_msg)

# Я - это ты, только короче

print(is_rd and 'Ready' or 'You are non repaired!!!')

# Я - это ты, только без тройки по инфе

print('Ready' if is_rd else 'You are non repaired!!!')
