import uuid, random, jsonlines, logging, argparse
from datetime import datetime, date, timedelta
from dateutil import relativedelta
import ujson as json
from tqdm import tqdm
from nltk.corpus import names 
import numpy as np
from pytorch_pretrained_bert.tokenization import BertTokenizer
from nltk.corpus import words, wordnet
import nltk
nltk.download('words')
nltk.download('names')
male_names = names.words('male.txt')
female_names = names.words('female.txt')
names = male_names + female_names
things = ['apple', 'mango', 'ball', 'plate', 'dish', 'mask', 'hand-sanitizer', 'blue', 'green', 'red', 'pink', 'purple'
          'mop', 'doll', 'computer', 'doll', 'shampoo', 'bag', 'purse', 'table', 'chair', ]
logistics = ['height', 'weight', 'scores', 'age']
parties = ['aam-aadmi', 'bjp', 'congress', 'republic', 'democratic', 'shiv-sena']
genres = ['comedy', 'horror', 'romantic', 'drama']
treaties = ['nobel' ,'peace', 'h1b', 'visa']

# create logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

# words with <= 2 wordpieces
nltk_words = [w.lower() for w in words.words() if len(bert_tokenizer.tokenize(w)) <= 2]
#print(nltk_words)

superlatives = {'max':["longest", "last", "highest", "largest", "most"], 
                'min':["shortest", "first", "smallest", "lowest", "least"]}

comparatives = {'less': ["fewer", "less", "before", "earlier", "smaller", "lower", "shorter"],
                'more': ["more", "later", "bigger", "higher", "longer", "larger", "greater", "taller"]}

date_superlatives = {'max':["last", "latest", "most recent", "youngest"], 
                    'min':["first", "earliest", "oldest", 'least recent']}

date_comparatives = {'less': ["before", "earlier", "older"],
                     'more': ['after', "later", "younger"]}


# def rand_expression(args):
#     # returns arithmetic expression, val
#     if len(args) == 1:
#         return str(args[0]), args[0]
#     split = random.randint(1, len(args)-1)
#     exp1, val1 = rand_expression(args[:split])
#     exp2, val2 = rand_expression(args[split:])
#     op = random.choice(['+', '-', '*']) #if len(str(val1*val2)) < 10 else random.choice(['+', '-'])
#     val = {'+': val1 + val2, '-': val1 - val2, '*': val1 * val2}[op]
#     return '(%s %s %s)' % (exp1, op, exp2), val # infix


def rand_float(x):
    # randomly add upto 2 decimal places
    precision = np.random.choice([0, 1, 2], p=[0.2, 0.4, 0.4])
    fractional_part = {0: 0, 1: random.randint(0, 9)*0.1, 2: random.randint(0, 99)*0.01}[precision]
    return x + fractional_part


def signed_expression(args):
    # returns signed combination, val
    expr, val = '', 0
    for a in args:
        sign = random.choice(['+', '-']) 
        val += {'+': a, '-': -a}[sign]
        expr += '%s %s ' % (sign, str(a))
    expr = expr[1:] if expr[0] == '+' else expr
    return expr.strip(), round(val, 2)


def min_max_avg_expression(args):
    # returns min/max expression, val
    expr, val = '', 0
    choice = random.randint(0,2)
    val = [max(args), min(args), round(sum(args)/len(args), 2)][choice]
    expr = ', '.join(map(str, args)).strip()
    question_list = ['find the '+ [random.choice(superlatives['max']), random.choice(superlatives['min']), 
                        random.choice(['average', 'mean'])][choice] + ' of ',
                    'what is the ' + [random.choice(superlatives['max']), random.choice(superlatives['min']), 
                        random.choice(['average', 'mean'])][choice] + ' of ']
    question = question_list[random.choice([0,1])] + expr + ' ?' if random.choice([0,1]) else '%s(%s)' % ([random.choice(superlatives['max']), random.choice(superlatives['min']), 
                        'average','mean'][choice], expr)
    persons = [random.choice(names) for i in range(len(args))]
    persons = ','.join(map(str, persons)).strip()
    logi = random.choice(logistics)
    question1 = 'there are ' + str(len(args)) + ' people namely '  + persons + ' their ' + logi + ' are ' + expr + ' find the '+  [random.choice(superlatives['max']), random.choice(superlatives['min']), 
                        random.choice(['average', 'mean'])][choice] + " of " + logi + "."
    question = question if random.choice([0,1]) else question1
    #print(question)
    expr = '%s(%s)' % ([random.choice(superlatives['max']), random.choice(superlatives['min']), 
                        'average','mean'][choice], expr)
    return question, expr.strip(), val


def arg_min_max_expression(wrds, args, names):
    # returns argmin/argmax expression, val
    expr = ''
    choice = random.choice([0,1])
    logi = random.choice(logistics)
    f_args = wrds if choice else names
    find = ['maximum', 'minimum']
    max_or_min = random.randint(0,1)
    for w, a in zip(f_args, args):
        expr += '%s %s, ' % (w, str(a))
    question1 =  logi + ' of people ' + ' is given by ' + expr + 'who among them has ' + find[max_or_min] + " " + logi 
    question2 = ' the count of things is given by ' + expr + ' which of them has ' +  find[max_or_min] + " count"
    print(question1)
    question = question2 if choice else question1
    mn, mx, expr = min(args), max(args), expr[:-2].strip()
    val = f_args[args.index(mx)] if max_or_min else f_args[args.index(mn)]
    expr = '%s(%s)' % ('argmax' if max_or_min else 'argmin', expr)
    return question, expr.strip(), val


def rand_percent():
    # returns argmin/argmax expression, val
    # sample 3-5 args
    choice = random.choice([0,1])
    wrds1 = [random.choice(parties)
            for _ in range(np.random.choice([3, 4, 5], p=[0.2, 0.4, 0.4]))]
    wrds2 = [random.choice(genres)
            for _ in range(np.random.choice([3, 4, 5], p=[0.2, 0.4, 0.4]))]
    wrds = wrds1 if choice else wrds2
    args = []
    for p in np.random.dirichlet(np.ones(len(wrds)))*100:
        p = {0:float, 1: int}[random.randint(0,1)]((round(p, random.randint(1,2))))
        args.append(p)
    args[0] = round(100 - sum(args[1:]), 2)
    context = ''
    for w, a in zip(wrds, args):
        context += '%s %s%%, ' % (w, str(a))
    print(context)
    context = context[:-2].strip()
    question1 = 'the votes recieved by the participating parties are ' + context
    question2 = 'movies produced this year were ' + context
    question = question1 if choice else question2
    n_q_args = min(np.random.choice([1, 2, 3], p=[0.4, 0.3, 0.3]), len(args) - 1)
    print(n_q_args)
    q_ids_wrds = random.sample(list(enumerate(wrds)), n_q_args)
    print(q_ids_wrds)
    q_args, q_wrds = [], []
    for tup in q_ids_wrds:
        q_args.append(args[tup[0]]); q_wrds.append(tup[1])
    negate = random.choice(['', 'not '])
    question1 = ' what is the percentage of votes ' + negate + ' recieved by ' + ','. join(q_wrds) 
    question2 = ' what is the percentage of movies that are ' + negate + ','.join(q_wrds)
    question += question1 if choice else question2
    q = 'percent %s' % negate + ', '.join(q_wrds)
    expr = q + ' :: ' + context
    val = {'': sum(q_args), 'not ': 100 - sum(q_args)}[negate]
    return question, expr.strip(), context.strip(), q.strip(), round(val, 2), args


def date_min_max(n_args=3):
    # returns min/max expression, val, args
    people = [random.choice(names) for _ in range(n_args)]
    person = ','.join(people)
    rds = [datetime.now() - timedelta(days=2018*365) * random.random() for _ in range(n_args)]
    day_diff_range = 30 if random.randint(0,1) else 150
    diffs = random.sample(range(1, day_diff_range+1), n_args-1)
    for i in range(1, len(rds)):
        rds[i] = rds[0] + random.choice([-1,1]) * timedelta(days=diffs[i-1])
    random.shuffle(rds)
    choices = [[rd.strftime("%d %B %Y"), rd.strftime("%B %d, %Y")][random.randint(0, 1)] for rd in rds]
    print(choices)
    expr, max_or_min = '; '.join(choices).strip(), random.randint(0,1)
    young_old = ['older', 'younger']
    question = 'The birthdays of '  + person + ' are ' + expr + ' who is ' + young_old[max_or_min] + ' of the two'
    rd = [max(rds), min(rds)][max_or_min]
    print(choices)
    print(rd)
    val = people[rds.index(rd)]
    expr = '%s(%s)' % ([random.choice(date_superlatives['max']), 
                        random.choice(date_superlatives['min'])][max_or_min], expr)
    return question, expr.strip(), val, choices


def date_diff(typ=''):
    # returns expression, val, args
    people = [random.choice(names) for _ in range(2)]
    treats = [random.choice(treaties) for _ in range(2)]
    person = ','.join(people)
    treat = ','.join(treats)
    question1 = ' There are 2 people. ' + person + ' Their birthday are ' 
    question2 = 'These are the 2 treaties ' + treat + ' They were signed on '
    typ = typ if typ else random.choice(['years', 'months', 'days'])
    rds = [datetime.now() - timedelta(days=2018*365) * random.random() for _ in range(2)]
    if typ in ['months', 'days']:
        diff = timedelta(days=60) if random.randint(0,1) else timedelta(days=200)
        rds[1] = rds[0] + random.choice([-1,1]) * diff * random.random()
    random.shuffle(rds)
    choices = [[rd.strftime("%d %B %Y"), rd.strftime("%B %d, %Y")][random.randint(0, 1)] for rd in rds]
    # DROP: yr diff depends only on yr vals, similarly for months within an yr
    diff_years = max(rds).year - min(rds).year
    diff_months = diff_years*12 + (max(rds).month - min(rds).month)
    diff_days = (max(rds) - min(rds)).days
    val = {'years':diff_years, 'months':diff_months, 'days':diff_days}[typ]
    expr = '; '.join(choices).strip()
    question1 += expr + ' What is the difference in their age in ' + typ 
    question2 += expr + ' after how much time was another treaty signed in ' + typ
    question = question1 if random.choice([0,1]) else question2
    expr = 'difference in %s(%s)' % (typ, expr)
    return question, expr.strip(), val, choices

def triangle_questions():
    x = random.randint(0, 80)
    y = random.randint(0, 80)
    question = ' The two angles of a triangle are ' + str(x) + ' and ' + str(y) + 'respectively ' 
    question += ' what is the third angle '
    val = 180 - x - y
    expr = "120 - " + str(x) + '-' + str(y)
    knowledge = 'angles of a trainge sum to 180'
    return question, expr, knowledge,val

def speed_distance():
    units = ['km', 'm']
    times = ['hr', 's']
    speed = ['km/hr', 'm/s']
    vehicle = ['bus', 'car']
    choice = random.choice([0,1])
    dist = random.randint(1, 100)
    time = random.randint(1, 250)
    speed_unit = random.choice(speed)
    speed_idx = speed.index(speed_unit)
    question = 'There is a ' + random.choice(vehicle) + ' covering ' + str(dist) + units[choice] + ' in ' + str(time) + str(times[choice])  
    question += ' Find speed in ' + speed_unit
    knowledge = 'Speed is distance covered in unit time. 1km = 1000m and 1 hr = 60 sec'
    if choice == speed_idx:
        val = str(dist/time) + speed[speed_idx]
        expr = str(speed) + "/" + str(time)
    else:
        if choice == 1 and speed_idx == 0:
            val = str(dist/time * 3.6) + speed[speed_idx]
            expr = str(dist) + "/" + str(time) + "*" + "3.6"
        elif choice == 0 and speed_idx == 1:
            val = str(dist/time * 0.28) +  speed[speed_idx]
            expr = str(dist) + "/" + str(time) + "*" + "0.28"
    return question, expr, val, knowledge

def main():
    parser = argparse.ArgumentParser(description='For generating synthetic numeric data.')
    parser.add_argument("--num_samples", default=1e6, type=float, help="Total number of samples to generate.")
    parser.add_argument("--num_dev_samples", default=1e4, type=float, help="Num of samples to keep aside for dev set.")
    parser.add_argument("--output_jsonl", default='synthetic_numeric.json', type=str, 
                        help="Output synthetic numeric data .jsonl file.")
    pargs = parser.parse_args()
    
    # split the domain
    domain, train_number_range, dev_number_range = int(2e4), [], []
    for i in range(domain):
        x = train_number_range if random.random() < 0.8 else dev_number_range
        x.append(i)
    
    #print(train_number_range)
    #print(dev_number_range)
    n_examples, n_dev, q_types = int(pargs.num_samples), int(pargs.num_dev_samples), 6
    discrete_ops_data, n_iters = [], n_examples // q_types
    train_args, dev_args = set(), set()

    logger.info(f"Creating {n_examples} samples...")
    for i_s in tqdm(range(n_iters)):
        # decide train/dev split
        split = 'train' if i_s < n_iters - (n_dev // q_types) else 'dev'
        rng = {'train': train_number_range, 'dev': dev_number_range}[split]
        args = [random.choice(rng) for _ in range(np.random.choice([2, 3, 4], p=[1/3]*3))]
        # with 50% prob add rand fraction
        args = list(map(rand_float, args)) if random.randint(0,1) else args
        print("these are args")
        print(args)
        train_args.update(args) if split == 'train' else dev_args.update(args)

        wrds = [random.choice(things) for _ in range(len(args))]
        people = [random.choice(names) for _ in range(len(args))]

        expr, val = signed_expression(args)
        d1 = {'id': str(uuid.uuid4().hex), 'passage': '', 'question': expr, 'equation_expression': expr, 'answer': val, 
              'type': 'RT_Template_Based_Generation', 'reasoning_type': 'addition subtraction operations'}

        question, expr, val = min_max_avg_expression(args)
        d2 = {'id': str(uuid.uuid4().hex), 'passage': '', 'question' :question,  'equation_expression': expr, 'answer': val, 
              'type': 'RT_Template_Based_Generation', 'reasoning_type': 'min max avg operations'}

        question, expr, val = arg_min_max_expression(wrds, args, people)
        d3 = {'id': str(uuid.uuid4().hex),'passage':'', 'question' : question, 'equation_expression': expr, 'answer': val,  
              'reasoning_type': 'arg_min_max_expression', 'type': 'RT_Template_Based_Generation', 'knowledge': ''}

        question, expr, val, date_args = date_min_max(n_args=len(args))
        d4 = {'id': str(uuid.uuid4().hex),'passage':'','question': question, 'equation_expression': expr, 'answer': val, 
              'type': 'RT_Template_Based_Generation', 'reasoning_type': 'max,min of dates', 'knowledge': ''}

        question, expr, val, date_args = date_diff()
        d5 = {'id': str(uuid.uuid4().hex),'passage':'','question': question,'equation_expression': expr, 'answer': val, 
              'type': 'RT_Template_Based_Generation', 'reasoning_type': 'date difference', 'knowledge': ''}

        question, expr, context, qn, val, args = rand_percent()
        d6 = {'id': str(uuid.uuid4().hex),'passage': '', 'question': question ,'equation_expression': expr, 'answer': val, 
             'type': 'RT_Template_Based_Generation' , 'reasoning_type': 'percentage', 'knowledge': 'Sum of all percentage is 100'}
        
        question, expr, knowledge, val = triangle_questions()
        d7 = {'id': str(uuid.uuid4().hex), 'passage': '','question': question, 'equation_expression' : expr, 'knowledge': knowledge, 'answer': val, 'reasoning_type' : 'geometry', 'type': 'RT_Template_Based_Generation' }
        
        question, expr, val, knowledge = speed_distance()
        d8 = {'id' : str(uuid.uuid4().hex) ,'passage': '', 'question': question, 'equation_expression': expr, 'knowledge': knowledge, 'answer': val, 'reasoning_type' : 'speed-distance-time', 'type': 'RT_Template_Based_Generation'}

        discrete_ops_data += [d1, d2, d3, d4, d5, d6, d7, d8]

    assert train_args.isdisjoint(dev_args) # trn, dev args are disjoint

    with jsonlines.open(pargs.output_jsonl, mode='w') as writer:
        writer.write_all(discrete_ops_data)
    

if __name__ == "__main__":
    main()
    
    
'''
python gen_numeric_data.py --num_samples 1e6 --num_dev_samples 1e4 --output_jsonl ../data/synthetic_numeric.jsonl
'''