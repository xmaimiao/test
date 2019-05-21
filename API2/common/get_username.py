from API2.common.context import Context
import random,string
import re

class UserName:
    def user_name(self):
        seq1 = string.ascii_letters
        seq2 = string.digits
        username = 'test_' + random.choice(seq1) + str(random.choice(seq2))
        setattr(Context,'username',username)

    def replace_name(self,title):
        before_code = re.search('(\d+)', getattr(Context, 'username')).group(1)
        if '重複' in title:
            username = getattr(Context, 'username')
        else:
            username = getattr(Context, 'username')[:6] + str(int(before_code) + 1)
            setattr(Context, 'username', username)

        return username

if __name__ == '__main__':
    user =UserName()
    print(user.user_name())
