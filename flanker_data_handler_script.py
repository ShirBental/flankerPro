from round import Round
data_path='data.csv'

def handle_round(current_round, rounds):
    rounds.append(Round(current_round,rounds))
    if len(rounds)>1:
        rounds[-2].complete_click_duration(rounds[-1])


def handle_single_row(row):
    user_data=[]
    rounds=[]
    is_user_data=True
    current_round= None
    for v in row:
        if 'Round' in v:
            is_user_data=False
            if current_round is not None:
                handle_round(current_round, rounds)
            current_round=[]
        if is_user_data:
            user_data.append(v)
        else:
            current_round.append(v)
    return user_data, rounds

with open(data_path,'rb') as reader:
    raw_text=reader.read()
    for row in raw_text.split('\n'):
        user_data, rounds = handle_single_row(row.strip().split(','))
