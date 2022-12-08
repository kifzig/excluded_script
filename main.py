
#This script takes a list of emails created from a Salesforce report for candidates on an opportunity.
import pandas as pd

#List of emails to delete is CSV - single column - column name is Primary Email
df_emails20 = pd.read_csv('emails.csv')

#Blast List of Contacts from Salesforce = Email column is Primary Email
df_not_excluded = pd.read_csv('phoenix.csv')

print("NUMBER ON LIST BEFORE: ", len(df_not_excluded.index))

for value in df_emails20['Primary Email'].items():
    email_to_delete = value[1]
    print(email_to_delete)
    df_not_excluded = df_not_excluded[df_not_excluded['Primary Email'] != email_to_delete]

df_excluded = df_not_excluded

print("NUMBER ON LIST AFTER ROWS DELETED: ", len(df_excluded.index))

df_excluded.to_csv('phoenix_excluded.csv')