#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[5]:


import pandas as pd
import numpy as np


# In[61]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[31]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[3]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return int(black_friday[(black_friday.Gender.isin(['F'])) & (black_friday.Age.isin(['26-35']))].shape[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday.User_ID.unique().shape[0]


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return pd.unique(black_friday.dtypes.tolist()).shape[0]


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return black_friday[black_friday.isna().any(axis=1)].shape[0]/black_friday.shape[0]


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    r = black_friday.isna().sum().max()
    return int(r)
    


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    a = black_friday.groupby("Product_Category_3").count()[["User_ID"]]
    a = a[a.User_ID == a.User_ID.max()]
    a = a.index.tolist()
    return int(a[0])


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[81]:


def q8():
    # Retorne aqui o resultado da questão 8.
    black_friday["Purchase2"] = (black_friday["Purchase"]-black_friday["Purchase"].min())/(black_friday["Purchase"].max()-black_friday["Purchase"].min())
    return float(black_friday["Purchase2"].mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[39]:


def q9():
    # Retorne aqui o resultado da questão 9.
    black_friday["Purchase_n"] = (black_friday["Purchase"]-black_friday["Purchase"].mean())/black_friday["Purchase"].std()
    r = black_friday["Purchase_n"][(black_friday["Purchase_n"] >= -1) & (black_friday["Purchase_n"] <= 1)]
    return int(r.count())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return True


# In[ ]:




