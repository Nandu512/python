has_account=True
email_verified=False
can_login=has_account and email_verified
email='abhi@gmail.com'
email_valid='@' in email
user_age=17
_age_valid=user_age>=18
can_login_final=has_account and email_verified and email_valid
print('can login(basic):',can_login)
print('email valid:',email_valid)
print('age valid:',_age_valid)
print('can login (final):',can_login_final)
i=has_account is True
print('has account is true:',i)