# Authors: Grant Doan and Zain Mirza (zainmirza and doanlng)
import time, binascii, itertools, hashlib # packages for time, hashing, iteration, hashing respectively
import matplotlib # package for plotting
from matplotlib import pyplot as plt    #plotting package from within matplotliv
dict_file = open('dictionary.txt', 'r')
dict_array = []
for line in dict_file:
  dict_array.append(line.rstrip('\n')) # rstrip('\n') removes newline characters from the words

print(dict_array)

X_POINT_MARGIN = .001   #x margin for x points on pyplot
Y_POINT_MARGIN = .0004  #y margin for y points on pyplot

#lists necessary for plotting and data storage
timeList = [] #list with times for each guess
guessList = [] #list with guess number amounts
lenList = [] #list for each

#hashes user password
def hashword(word):
    #this is the secure hash function that actually hashes the user password, using params that specify hashname, salt type
    hashed = hashlib.pbkdf2_hmac(sha, #static hashing algorithm we use at first but will change later to user specification
                                word.encode('utf-8'), #encodes word to binary
                                'salty'.encode('utf-8'),
                                 1)    #recomended iterations for sha256
    return binascii.hexlify(hashed) #return word in hex

passwords_arr = [] #all the passwords run through dictionaryAttack for display purposes
def dictionaryAttack(password):
    lenPassword = len(password)
    lenList.append(lenPassword)
    print('Password is: ' + password + ', Password length is ' + str(lenPassword))
    passwords_arr.append(password)
    start = time.time()
    hashed_pwd_hex = hashword(password)
    amountOfWords = 1  # this is the amount of words in the password that we assume, we will increment it if we find out
                       # that it is more than 1
    attempts = 0
    multipleWords = False   #this is here allow us to reiterate through the dictionary
    while not multipleWords:  # this allows us to know how many words are in the password. i.e if the for loop runs to
                        # completion and found is still false, then it is more than 1 word
        guesses = itertools.permutations(dict_array, amountOfWords)  # grabs all combinations of words in the dict_array given the amount of words, i
        for word in guesses:
            guess = str(''.join(word))  # joins each tuple making it into a single string
            if (len(guess) == lenPassword):  # compares each string
                if (hashword(guess) == hashed_pwd_hex):
                    print("Guessed it! " + str(''.join(word)) + ' in ' + str(attempts) + ' guesses')
                    multipleWords = True
                    break  # break from the loop once the word is guessed (saves on efficiency)
                else:
                    attempts += 1
        amountOfWords += 1
    guessList.append(attempts)  # append number of guesses for this word
    # Hint5: measuring time difference.
    total_time = time.time() - start
    timeList.append(total_time)
    print("Elapsed time: ", str(total_time) + " seconds.")

pw = input("Enter a password: ")# accept user input
lenPassword = len(pw) #word length
sha = input('Enter 1 for SHA256 or anything else for SHA512')
if sha == '1':
    sha = 'sha256'
else:
    sha = 'sha512'
dictionaryAttack(pw) #launches first dictionary attack with user inputted password

#hardcoded examples for plotting
print('Now trying hardcoded examples...')
dictionaryAttack('111111footbalninja')
dictionaryAttack('iloveyoubaseballjesus')
dictionaryAttack('password1mustangabc123')
dictionaryAttack('ninjamonkeyjesus')
dictionaryAttack('shadowpassword1baseball')
dictionaryAttack('trustno1passwordninja')
dictionaryAttack('master123123password1')
dictionaryAttack('masterabc123ashley')
dictionaryAttack('mustangbaseballdragon')
print('Plotting data (including user input) now...')

#plotting lists
plt.plot(lenList, timeList, 'o', color = 'black') #plot these 2 lists, lenList is x axis, timelist is y
plt.title('Time Taken to Guess vs Word Length in ' + str(sha).upper() + ' with Dictionary Size: 25')#title
plt.xlabel('Word length in chars')  #label x
plt.ylabel('Time it took to guess in s')    #label y
for nElem in range(len(passwords_arr)):
        plt.text(lenList[nElem] + X_POINT_MARGIN, timeList[nElem] + Y_POINT_MARGIN, passwords_arr[nElem], fontsize = 'xx-small', horizontalalignment = 'center')   #label each point with a name
plt.show()  #show plot