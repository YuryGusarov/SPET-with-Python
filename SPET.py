#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Enter your Human Genome SNP")
Input_DNA = input()
print(type(Input_DNA))
logpas = {
    "uname": 'def', 
    "upasswd": 'def'
}
login = input('Enter email: ')
passwd = input('Password: ')
logpas['uname'] = login
logpas['password'] = passwd
url = 'https://www.ncbi.nlm.nih.gov/account/?back_url=https%3A%2F%2Fwww.ncbi.nlm.nih.gov%2F'
s = requests.Session()
loging = s.post(url, data = logpas)

# In[ ]:




