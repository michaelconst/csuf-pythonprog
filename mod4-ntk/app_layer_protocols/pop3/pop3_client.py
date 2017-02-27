import poplib
import re


pop_client = poplib.POP3_SSL('pop.gmail.com')
pop_client.user('mconstantin@fullerton.edu')
pop_client.pass_('$harplabs2017')

num_msgs, msgs_size = pop_client.stat()

print('your mailbox has {} messages, for a total size of {}'.format(num_msgs, msgs_size))

for msg_id in range(1, num_msgs+1):
    for mail in pop_client.retr(msg_id)[1]:
        if re.search('Subject:', mail):
            print(mail)

pop_client.quit()