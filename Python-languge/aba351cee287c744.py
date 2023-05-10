atoz = 'abcdefghijklmnopqrstuvwxyz'
num_atoz = 26

def generate_key(A_number): # A에 해당하는 숫자를 리턴(return)
    return A_number%num_atoz + 1

def encrypt(key, msg):
    cipher = msg
    for char in atoz:
        cipher = cipher.replace(char, ' '+str(key)+',')
        key = key%num_atoz + 1 # key가 0이 되는 상황을 방지하기 위해 % 사용

    return cipher

def decrypt(key, cipher):
    msg = cipher
    for char in atoz:
        msg = msg.replace(' '+str(key)+',', char)
        key = key%num_atoz + 1

    return msg


my_key = 15

print("atoz를 암호화하면: ", encrypt(my_key, atoz))
print("다시 복호화하면: ", decrypt(my_key, atoz))
